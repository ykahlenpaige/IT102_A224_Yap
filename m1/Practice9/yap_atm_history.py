def view_history():

    try:

        with open("transactions.txt", "r") as file:

            lines = file.readlines()

        return lines

    except FileNotFoundError:

        return []

""" 
######### Learning Signature ######### 
Programmed by: Kahlen Yap
Date Submitted: September 9, 2026
 
Program Description: This program ____.
Reflection: I learned ____.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
﻿"""