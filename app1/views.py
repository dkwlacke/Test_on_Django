from django.shortcuts import render


def mini_calc(request):
	result,n1,n2 = 0,0,0
	context = {}

	if request.method == 'POST':
		n1 = request.POST.get('num1')
		n2 = request.POST.get('num2')
		op = request.POST.get('operation')
		if op == 'add':
			result = float(n1)+float(n2)
		elif op == 'multi':
			result = float(n1)*float(n2)
		elif op == 'div':
			result = float(n1)/float(n2)
		else:
			result = float(n1) - float(n2)
	context = {
		'res': result,
		'num1':n1,
		'num2':n2
	}
	return render(request,'calc.html',context)




