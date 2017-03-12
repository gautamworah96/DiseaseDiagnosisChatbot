from django.shortcuts import render, redirect, render_to_response
import apiai
import json,requests


from Main.models import main,symptoms

# Create your views here.
def index(request):
	domain = "https://api.api.ai/v1/"
	client_base = "65b21fedac084c16a9098ea44674270a"
	ai = apiai.ApiAI(client_base)
	choice='yes'
	while(choice!='no'):
		msg=input("enter the question \n")
		request = ai.text_request()
		request.session_id = "spitdisease12"
		request.query = msg
		response = json.loads(request.getresponse().read().decode('utf-8'))
		result = response['result']
		action = result.get('action')
		render_to_response('Main/intro.html', locals())

		if action=='getinfo':
			disease=response['result']['parameters']['disease']
			print('entered for loop for getinfo disease is  '+ disease)
			result_obj=main.objects.filter(name__icontains=disease)
			#print(result_obj)
			for j in result_obj:
				print((j.discription+'\n').encode("utf-8"))


		elif action=='getdiag':
			disease=response['result']['parameters']['disease']
			for i in disease:
				print('entered for loop for getdiag')
				#main.objects.raw('SELECT id from MAIN WHERE name LIKE ')


		#USED FOR FINDING WHAT ARE THE SYMPTOMS OF A PARTICULAR DISEASE
		elif action=='symptoms':
			disease=response['result']['parameters']['disease']
			for i in disease:
				print('entered for loop for symptoms')
				print('The symptoms for ' +i+ ' are: ')
				#obj=Symptoms.objects.raw('SELECT * FROM SYMPTOMS WHERE d_id IN (SELECT id FROM Main WHERE name LIKE '%gau%')',[i])
				mainobj=main.objects.filter(name__icontains=i)
				print(mainobj)
				for j in mainobj:
					print("entered and looping thru symtoms for id")
					obj=symptoms.objects.filter(d_id__in = mainobj.id)
					print(obj.symptom)

		elif action=='treatment':
			disease=response['result']['parameters']['disease']
			#for i in disease:
			print('entered for loop for treatment ' +str(disease))
			for i in disease:
				result_obj=main.objects.filter(name__icontains=i)[:2]
				#print(main.objects.all())
				#print(result_obj)
				for j in result_obj:
					print(j.treatment+'\n')

		elif action=='disease_cause':
			disease=response['result']['parameters']['disease']
			for i in disease:
				print('entered for loop for disease_cause')
				result_obj=main.objects.filter(name__icontains=disease)
				for j in result_obj:
					print(j.cause)

		print(result.get('metadata').get('intentName'))
		print(response['result']['parameters']['disease'])
		choice=input('yes to continue no to exit the chatbot ')
	return render_to_response('Main/intro.html', locals())


'''

{
	"id": "b3b82aff-1392-41ea-a3e9-05717250bbbb",
	"timestamp": "2017-03-08T18:54:17.553Z",
	"lang": "en",
	"result": {
		"source": "agent",
		"resolvedQuery": "WHat is Cancer ?",
		"action": "getinfo",
		"actionIncomplete": false,
		"parameters": {
			"disease": "cancer"
		},
		"contexts": [
			{
				"name": "disease",
				"parameters": {
					"disease.original": "Cancer ?",
					"disease": "cancer"
				},
				"lifespan": 5
			}
		],
		"metadata": {
			"intentId": "8b2e56dc-7cb9-4e3e-9f02-3f31b8bb6233",
			"webhookUsed": "false",
			"webhookForSlotFillingUsed": "false",
			"intentName": "Get Disease Information"
		},
		"fulfillment": {
			"speech": "",
			"messages": [
				{
					"type": 0,
					"speech": ""
				}
			]
		},
		"score": 1
	},
	"status": {
		"code": 200,
		"errorType": "success"
	},
	"sessionId": "spitdisease"
}

'''
