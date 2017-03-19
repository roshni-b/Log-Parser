#! /usr/bin/env/python
import time as t1

class Log_Parsing:
	log_file = "" # input file
	processed_log_file = "" # intermediate after pre-processing input
	final_file = "" # final result file

	def get_files(self):
		"""Asks user to input a raw .tsv log file and pre-processes it to store in an intermediate .csv file."""
		self.log_file = str(raw_input("Enter log file name: ")) # Ask user to input file name with extension
		self.processed_log_file = self.log_file+"_processed_input.csv" 
		self.final_file = self.log_file+"_result_file.csv"
		
		# Extracting raw log files and pre-processing to fix incorrect records
		with open (self.log_file, "r") as f: # Reading from input .tsv file
			with open(self.processed_log_file, "w+") as t: # Writing into intermediate .csv file
				for line in f:
					line = line.replace(",", ".") # Inconsistant hostnames are fixed by replacing commas with dots
					k = line.strip().split()
					for i in range(len(k)):
						t.write(k[i]+",")
					t.write("\n")

					
	def log_parser(self):
		"""Parses data from the pre-processed input .csv file, assigns session IDs, and stores the parsed data in an output .csv file. """
		mins = 0 # time in minutes
		count = 0
		d = {} # Dictionary to keep track of the different hosts and their sessions
		delim = "," # Delimiter for output file

		with open(self.processed_log_file, "r") as f: # Reading from intermediate .csv file
			with open(self.final_file, "w+") as t: # Writing into final output .csv file
				for line in f:
					if(count==0):
						t.write("host,sessionID,date (DD-MM-YYYY),time (HH:MM:SS),method,response\n") # Header of table
						count = 1
					else:
						temp = 0
						k = line.strip().split(",")
						if(k[0] not in d): 
							# For every newly encountered host name, key=host and  value=(time in mins, x=1) is assigned to it's dictionary entry
							d[k[0]] = (int(k[2].strip())/60, 1)
						else:
							# For hosts existing in the dictionary, if (current activity time - previous activity time) > 15, value=(current time in mins, x+=1)
							mins = int(k[2].strip())/60
							if((mins - d[k[0]][0]) > 15): # A session lasts 15 mins
								temp = d[k[0]][1]
								temp += 1
								d[k[0]] = (int(k[2].strip())/60, temp)
								
						time = t1.strftime('%d-%m-%Y,%H:%M:%S', t1.localtime(int(k[2].strip()) - 37800)) # Conversion of given timestamp. IST-GMT = 37800 seconds
						session_id = k[0] + "_" + str(d[k[0]][1]) # Session ID is assigned from the dictionary value, in the format hostname_x
						s = k[0] + delim + session_id + delim + str(time) + delim + k[3]+ delim + k[5]
						t.write(s+"\n")

parser_obj=Log_Parsing()
parser_obj.get_files()
parser_obj.log_parser()