from django.shortcuts import render
from datetime import datetime

def task_view(request):
    # Dynamic data for the template
    context = {
        'user_name': 'Venugopal K',
        'user_role': 'Developer',
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'tasks': [
            {'name': 'Complete Django Project', 'status': 'in-progress'},
            {'name': 'Review Code', 'status': 'pending'},
            {'name': 'Write Tests', 'status': 'completed'},
            {'name': 'Deploy Application', 'status': 'pending'},
            {'name': 'Update Documentation', 'status': 'completed'},
        ],
        'total_tasks': 5,
        'completed_tasks': 2,
        'pending_tasks': 3,
    }
    return render(request, 'task.html', context)
