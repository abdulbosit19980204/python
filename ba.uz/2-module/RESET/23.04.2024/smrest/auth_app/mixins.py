from rest_framework.generics import (ListAPIView, CreateAPIView,
                                     RetrieveAPIView, UpdateAPIView, DestroyAPIView
                                     )


class UpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    pass



