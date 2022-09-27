from .models import SystemConfig, Department, ProgramGroup


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.system_config = {i.key: i.value for i in SystemConfig.objects.all()}
        request.departments = Department.objects.all()
        request.program_groups = ProgramGroup.objects.all()

        response = self.get_response(request)

        return response
