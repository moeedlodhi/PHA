from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from PHA.decorators import user_role

from societies.models import member_plots, society
from UserManagement.models import Users

# Create your views here.


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@user_role(['Admin'])
def create_allotment(request):

    try:
        society_id = request.POST['society_id']
        society_object = society.object.get(id=society_id)  # society object from society id
        user_id = request.POST['user_id']
        user_object = Users.objects.get(id=user_id)  # user object from user id
        member_plot_id = request.POST['member_plot_id']
        member_plot_object = member_plots.object.get(id=member_plot_id)  # member plot object from member plot id

        membership_no = request.POST['membership_no']
        society_no = request.POST['society_no']
        full_name = request.POST['full_name']
        block = request.POST['block']
        size = request.POST['size']
        type = request.POST['type']
        corner = request.POST['corner']
        res_com = request.POST['res_com']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        fh_type = request.POST['fh_type']
        fh_name = request.POST['fh_name']
        gender = request.POST['gender']
        cnic = request.POST['cnic']
        current_city = request.POST['current_city']
        profession = request.POST['profession']
        date_of_birth = request.POST['date_of_birth']
        plot_price = request.POST['plot_price']
        status = request.POST['status']
        allotment_letter = request.POST['allotment_letter']
        possession_letter = request.POST['possession_letter']
        digitizing_letter = request.POST['digitizing_letter']
        is_balloting = request.POST['is_balloting']
        is_auction = request.POST['is_auction']
        is_open = request.POST['is_open']
        is_proxy = request.POST['is_proxy']
        is_imported = request.POST['is_imported']
        is_exemption = request.POST['is_exemption']
        is_pgshf = request.POST['is_pgshf']
        comments = request.POST['comments']

    except:
        raise ValidationError('username or email missing')

    return Response({"message": "HAPPY"})
