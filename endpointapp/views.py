from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime, timedelta

def get_info(request):
    try:
        # Get query parameters from the URL
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        # Get the current day of the week
        current_day = datetime.now().strftime('%A')

        # Get the current UTC time with validation of +/-2 hours
        utc_time = (datetime.utcnow() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')

        # Format UTC time to match "2023-09-07T12:14:41Z"
        #- The utc time should be in this format : 2023-09-07T12:19:19Z
        utc_time = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%dT%H:%M:%SZ')

        # Get the GitHub file and repo URLs
        github_file_url = 'https://github.com/developerayyo/HNGTasks/blob/main/endpointapp/views.py'
        github_repo_url = 'https://github.com/developerayyo/HNGTasks'

        # Create the JSON response
        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
