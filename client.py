import socket
import sys

from PyQt5.QtCore import pyqtSignal, QObject
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import threading
import connect_dialog
import users
import groups
import pysfmgui
import datetime


def close_event(self):
	raise SystemExit


app = QApplication(sys.argv)
mainWindow = QMainWindow()
mainui = pysfmgui.Ui_MainWindow()
mainui.setupUi(mainWindow)
mainWindow.show()
mainWindow.closeEvent = close_event

connectdialog = QDialog(mainWindow)
connectui = connect_dialog.Ui_Dialog()
connectui.setupUi(connectdialog)
old_event = connectdialog.closeEvent
connectdialog.closeEvent = close_event

usersdialog = QDialog(mainWindow)
usersui = users.Ui_users()
usersui.setupUi(usersdialog)

groupsdialog = QDialog(mainWindow)
groupsui = groups.Ui_groups()
groupsui.setupUi(groupsdialog)


connection = None
contacts = {}
grouplist = {}


def get_groups():
	cmd = "showgroup"
	cmd = bytearray("/" + cmd, "UTF8")
	cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
	connection.send(cmd)


def get_members():
	name = groupsui.grouplist.currentItem().text()
	cmd = "showgroup " + name
	cmd = bytearray("/" + cmd, "UTF8")
	cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
	connection.send(cmd)


def get_users():
	cmd = "users"
	cmd = bytearray("/" + cmd, "UTF8")
	cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
	connection.send(cmd)


def get_onlineusers():
	cmd = "onlineusers"
	cmd = bytearray("/" + cmd, "UTF8")
	cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
	connection.send(cmd)


def delete_group():
	name = groupsui.grouplist.currentItem()
	if name is not None:
		name = name.text()
		cmd = "deletegroup " + name
		cmd = bytearray("/" + cmd, "UTF8")
		cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
		connection.send(cmd)
		groupsui.memberlist.clear()
		get_groups()


def create_group():
	name = groupsui.creategrouple.text()
	if name != "":
		cmd = "creategroup " + name
		cmd = bytearray("/" + cmd, "UTF8")
		cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
		connection.send(cmd)
		get_groups()
		groupsui.memberlist.clear()


def add_user():
	name = groupsui.adduserle.text()
	group = groupsui.grouplist.currentItem()
	print(str(name) + " " + str(group))
	if name != "" and group is not None:
		group = group.text()
		cmd = "addmember " + group + " " + name
		cmd = bytearray("/" + cmd, "UTF8")
		cmd = (len(cmd) + 1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
		connection.send(cmd)
		get_groups()
		groupsui.memberlist.clear()


class Signals(QObject):
	open_login_signal = pyqtSignal()
	set_groups_signal = pyqtSignal(list)
	set_members_signal = pyqtSignal(str, list)
	open_groups_signal = pyqtSignal()
	set_users_signal = pyqtSignal(list)
	open_users_signal = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.open_login_signal.connect(self.open_login)
		self.set_groups_signal.connect(self.set_groups)
		self.set_members_signal.connect(self.set_members)
		self.open_groups_signal.connect(self.open_groups)
		self.set_users_signal.connect(self.set_users)
		self.open_users_signal.connect(self.open_users)

	@staticmethod
	def open_login():
		connectdialog.exec()

	@staticmethod
	def open_groups():
		get_groups()
		groupsdialog.exec()

	@staticmethod
	def open_users():
		get_onlineusers()
		usersdialog.exec()

	@staticmethod
	def set_groups(groupargs):
		grouplist.clear()
		for group in groupargs:
			grouplist.update({group: []})
		groupsui.grouplist.clear()
		for group in grouplist:
			groupsui.grouplist.addItem(group)

	@staticmethod
	def set_members(groupname, memberlist):
		if groupname not in grouplist:
			print("Couldn't find " + groupname)
		else:
			grouplist[groupname] = memberlist
			groupsui.memberlist.clear()
			for member in memberlist:
				groupsui.memberlist.addItem(member)

	@staticmethod
	def set_users(users):
		usersui.userlist.clear()
		for user in users:
			usersui.userlist.addItem(user)


signals_object = Signals()


def get_sfm_message():
	to_read = connection.recv(2)
	if not to_read:
		return False
	to_read = int.from_bytes(to_read, byteorder='big')
	message = connection.recv(to_read)
	if message == b"\x00":
		return None
	else:
		return message


def command_handler(message):

	if message[:len("/status groups ")] == "/status groups ":
		items = message[len("/status groups "):].split(",")
		signals_object.set_groups_signal.emit(items)
	elif message[:len("/status groups")] == "/status groups":
		signals_object.set_groups_signal.emit([])
	elif message[:len("/status groupmembers ")] == "/status groupmembers ":
		tmp = message[len("/status groupmembers "):].split(" ")
		name = tmp[0]
		items = tmp[1].split(",") if len(tmp) == 2 else []
		signals_object.set_members_signal.emit(name, items)
	elif message[:len("/status users")] == "/status users":
		items = message[len("/status users "):].split(",")
		signals_object.set_users_signal.emit(items)
	elif message[:len("/status onlineusers")] == "/status onlineusers":
		items = message[len("/status onlineusers "):].split(",")
		signals_object.set_users_signal.emit(items)

class message_logging(QObject):
	incoming_message = pyqtSignal(str)

	def __init__(self):
		super().__init__()
		self.incoming_message.connect(self.message_logger)

	def message_receiver(self):
		while True:
			message = get_sfm_message()
			if message == False:
				self.incoming_message.emit("Connection closed.\n")
				connection.close()
				signals_object.open_login_signal.emit()
				return
			elif message is not None:
				if message[0] == 47:
					print(message.decode("utf-8").rstrip("\0"))
					command_handler(message.decode("utf-8").rstrip("\0"))
				else:
					output = "At: " + datetime.datetime.fromtimestamp(int.from_bytes(message[:8], byteorder='little')).strftime('%Y-%m-%d %H:%M:%S') + "\n"
					match = re.search(">.+@.+:", message[8:].decode("utf-8"))
					output += "From: " + match.group(0).rstrip(":").lstrip(">") + "\n"
					output += message[8:].decode("utf-8")[match.end():]
					self.incoming_message.emit(output)

	@staticmethod
	def message_logger(message):
		scroll = mainui.incmessageinput.verticalScrollBar()
		should_scroll = True if scroll.value() == scroll.maximum() else False
		mainui.incmessageinput.appendPlainText(message + "\n")
		if should_scroll:
			scroll.setValue(scroll.maximum())


message_logging_object = message_logging()


def serverconnect():
	global connection
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	targetserver = connectui.addressle.text()
	username = connectui.usernamele.text()
	password = connectui.passwordle.text()
	try:
		connection.connect((targetserver, 2000))
	except Exception as e:
		connectui.statusoutputlbl.setText("Error connecting to Server: " + str(e))
		return

	try:
		option = bytearray("1", "UTF8")
		option = (len(option)+1).to_bytes(2, 'big') + option + int(0).to_bytes(1, 'big')
		connection.send(option)

		username = bytearray(username, "UTF8")
		username = (len(username)+1).to_bytes(2, 'big') + username + int(0).to_bytes(1, 'big')
		connection.send(username)

		password = bytearray(password, "UTF8")
		password = (len(password)+1).to_bytes(2, 'big') + password + int(0).to_bytes(1, 'big')
		connection.send(password)
	except Exception as e:
		connectui.statusoutputlbl.setText("Error sending login information to Server: " + str(e))
		return

	answer = get_sfm_message()

	if answer.decode("utf-8").rstrip("\0") == "1":
		connectdialog.closeEvent = old_event
		connectdialog.close()
		threading.Thread(target=message_logging_object.message_receiver, daemon = True).start()
		return
	else:
		connectui.statusoutputlbl.setText("Server rejected login")
		connection.close()
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_message():
	targetserver = mainui.serverinput.currentText()
	targetuser = mainui.userinput.currentText()
	message = mainui.messageinput.toPlainText()
	mainui.messageinput.clear()

	message = bytearray(targetserver+"@"+targetuser+":"+message, "UTF8")
	message = (len(message)+1).to_bytes(2, 'big') + message + int(0).to_bytes(1, 'big')
	connection.send(message)


def send_command():
	cmd = mainui.cmdinput.currentText()
	cmd = bytearray("/" + cmd, "UTF8")
	cmd = (len(cmd)+1).to_bytes(2, 'big') + cmd + int(0).to_bytes(1, 'big')
	connection.send(cmd)


def add_contact():
	input1 = mainui.serverinput
	input2 = mainui.userinput
	if input1.currentText() not in contacts:
		contacts[input1.currentText()] = [input2.currentText()]
		input1.addItem(input1.currentText())
	else:
		if input2.currentText() not in contacts[input1.currentText()]:
			contacts[input1.currentText()].append(input2.currentText())


def user_contact():
	mainui.userinput.clear()
	if mainui.serverinput.currentText() in contacts:
		for contact in contacts[mainui.serverinput.currentText()]:
			mainui.userinput.addItem(contact)


connectui.quitbtn.clicked.connect(close_event)
connectui.connectbtn.clicked.connect(serverconnect)

mainui.sendbtn.clicked.connect(send_message)
mainui.contactbtn.clicked.connect(add_contact)
mainui.cmdbtn.clicked.connect(send_command)
mainui.serverinput.currentTextChanged.connect(user_contact)
mainui.showgroupbtn.clicked.connect(signals_object.open_groups_signal)
mainui.showusersbtn.clicked.connect(signals_object.open_users_signal)

groupsui.refreshbtn.clicked.connect(get_groups)
groupsui.grouplist.itemSelectionChanged.connect(get_members)
groupsui.deletegroupbtn.clicked.connect(delete_group)
groupsui.creategroupbtn.clicked.connect(create_group)
groupsui.adduserbtn.clicked.connect(add_user)

usersui.allusersbtn.clicked.connect(get_users)
usersui.onlineusersbtn.clicked.connect(get_onlineusers)

signals_object.open_login_signal.emit()
sys.exit(app.exec_())