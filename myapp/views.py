import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from myapp.constants import variable_styles

@csrf_exempt
def replace_variables(request):
    variables_to_replace = [
        'Site_id',
        'FieldreplaceableUnit_value(RRU-7)',
        'AntennaUnitGroup_value',
        'AntennaUnit_value',
        'AntennaSubunit_value',
        'EUtranCellFDD_value',
        'dlAttenuation_value',
        'dlTrafficDelay_value',
        'Exist-RfBranch_1',
        'Exist-RfBranch_2',
        'New-RfBranch_1',
        'New-RfBranch_2',
        'SectorCarrier_value',
        'SectorEquipmentFunction_value',
        
    ]

    if request.method == 'POST':
        # Read the static file
        static_file_path = os.path.join(settings.BASE_DIR, 'static', 'ret.txt')
        
        if not os.path.exists(static_file_path):
            return render(request, 'replace_variables.html', {'error': 'File not found in static folder.'})

        # Prompt the user to enter values for the variables
        variable_values = {var: request.POST.get(var, '') for var in variables_to_replace}

        # Replace variable names with their values in the file content
        with open(static_file_path, 'r') as input_file:
            input_text = input_file.read()
            for variable, value in variable_values.items():
                input_text = input_text.replace(variable, value)

        # Generate the output file
        output_file_name = "ret_output.txt"
        output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)

        with open(output_file_path, 'w') as output_file:
            output_file.write(input_text)

        # Generate the file URL for download
        output_file_url = os.path.join(settings.MEDIA_URL, output_file_name)

        return render(request, 'replace_variables.html', {'output_file_url': output_file_url})

    return render(request, 'replace_variables.html', {'variables_to_replace': variables_to_replace})
