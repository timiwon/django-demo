from rest_access_policy import AccessPolicy

class BaseAccessPolicy(AccessPolicy):
    def user_must_be(self, request, view, action, field: str) -> bool:
        obj = view.get_object()
        print(obj)
        return getattr(obj, field) == request.user