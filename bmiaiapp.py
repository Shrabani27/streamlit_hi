import google.generativeai as genai
genai.configuration(api_key="AIzaSyDJE-TNW2Vs0On2AHftdcH0uhJxPUrWlJw")
model = genai.GenerativeModel("gemini-2.5-flash")


name = input("Enter your name:")
wt = int(input("Enter your weight:"))
ht = int(input("Enter your height:"))    


bmi = round(wt / (ht/100)**2,2)
print("With your height:", ht, "and weight:", wt, "your BMI is:", bmi)
prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, and BMI as {bmi}"

response = model.generate_content(prompt)
print(response.text)
         
