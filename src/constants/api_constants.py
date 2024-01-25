# Enter your constant here


class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com/"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # PUT, PATCH, UPDATE AND DELETE = we need the booking ID so.

    def url_put_patch_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.bookingid)
