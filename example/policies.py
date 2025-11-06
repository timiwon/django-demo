from base_app.policies import BaseAccessPolicy

class ArticleAccessPolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["list"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["authenticated"],
            "effect": "allow"
        },
        {
            "action": ["retrieve", "update", "partial_update", "destroy"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": ["user_must_be:owner"],
        },
    ]
