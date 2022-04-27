import sqlite3
from colorama import init, Fore

init()

class Accounts:
	def __init__(self, loop):
		self.loop = loop
		self.CONNECTION = "accounts.db"

		self.create_db()
		self.LOOP()

	def create_db(self):
		self.conn = sqlite3.connect(self.CONNECTION)
		self.c = self.conn.cursor()

		self.c.execute("""CREATE TABLE IF NOT EXISTS accounts (
				social_net text,
				username text,
				password text
			)""")
		self.conn.commit()
		self.conn.close()

	def add_acc(self):
		self.conn = sqlite3.connect(self.CONNECTION)
		self.c = self.conn.cursor()

		self.snet = input("Social network: ")
		self.user = input("Username: ")
		self.pass_ = input("Password: ")

		self.c.execute("INSERT INTO accounts VALUES (:social_net, :username, :password)",
				{
					"social_net": self.snet,
					"username": self.user,
					"password": self.pass_
				}
			)

		self.conn.commit()
		self.conn.close()

		print(f"\n{Fore.GREEN}Social network added successfully")

	def delete_acc(self):
		try:
			id_input = int(input(f"ID>> "))
			self.conn = sqlite3.connect(self.CONNECTION)
			self.c = self.conn.cursor()

			self.c.execute(f"DELETE from accounts WHERE oid = {id_input}")

			self.conn.commit()
			self.conn.close()

			print(f"\n{Fore.GREEN}Successfully deleted account with ID: {id_input}")
		except:
			print(f"\n{Fore.RED}Insert a valid ID")

	def show_accs(self):
		self.conn = sqlite3.connect(self.CONNECTION)
		self.c = self.conn.cursor()

		self.c.execute("SELECT *, oid FROM accounts")
		record = self.c.fetchall()
		print("ID Social\t\tUser\t\t\tPassword\n")
		for i in record:
			print(f"{i[-1]}: {i[0]}\t\t{i[1]}\t\t\t{i[2]}")

		self.conn.commit()
		self.conn.close()


	def LOOP(self):
		while self.loop:
			print(f"""
 {Fore.BLUE}#1 {Fore.RESET}Add account
 {Fore.BLUE}#2 {Fore.RESET}Delete account
 {Fore.BLUE}#3 {Fore.RESET}Show all accounts
 {Fore.BLUE}#4 {Fore.RESET}Exit""")
			try:
				self.index = int(input(f">> "))

				if (self.index == 1):
					self.add_acc()

				elif (self.index == 2):
					self.delete_acc()

				elif (self.index == 3):
					self.show_accs()

				elif (self.index == 4):
					self.loop = False

				else:
					print(f"\n{Fore.RED}Insert a valid number")

			except:
				print(f"\n{Fore.RED}Insert a valid number")


Accounts(True)