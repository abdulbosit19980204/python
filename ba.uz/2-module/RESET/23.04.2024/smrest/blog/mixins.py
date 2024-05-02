from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView


class CreateDeleteUpdateAPIView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    pass


class UpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    pass
