from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Hello from Django backend!"})

def echo(request):
    if request.method == "POST":
        import json
        body = json.loads(request.body)
        return JsonResponse({"received": body})
    return JsonResponse({"error": "POST required"}, status=400)
