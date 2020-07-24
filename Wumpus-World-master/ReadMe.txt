
------------------------------------Read Me ------------------------------
LANGUAGE: Python
Code is written on PyCharm Ide
And ran on PyCharm terminal


 ----------------------------------CODE STRUCTURE --------------------------
Navigate yourself to task2 folder and open the .py files
Set of wumpus rules have been written
Knowledge file used was kb.txt

	
Method check_true_false() checks if the statement and its negation entail from the knowledge base. It uses TTCheckAll(),
which in-turn uses PLTrue() and extend. The output is print to a file called result.txt



---------------------------COMPILATION AND EXECUTION--------------------------------
	Execute check_true_false.py with standard python compilation commands (works on omega)

	It needs the following arguments:
		python check_true_false.py wumpus_rules.txt [additional_knowledge_file] [statement_file]