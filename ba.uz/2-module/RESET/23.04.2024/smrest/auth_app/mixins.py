from rest_framework.generics import (ListAPIView, CreateAPIView,
                                     RetrieveAPIView, UpdateAPIView, DestroyAPIView
                                     )


class CreateDestroyAPIView(CreateAPIView, DestroyAPIView):
    pass


class CreateUpdateAPIView(CreateAPIView, UpdateAPIView):
    pass
