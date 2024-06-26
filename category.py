import uuid
from datetime import datetime

class Category:
    def __init__(
        self,
        name,
        id = "",
        description = "",
        is_active = True,
    ):
        self.name = name,
        self.id = id or uuid.uuid4(),
        self.description = description,
        self.created_at = datetime.now()
        self.is_active = is_active,

    def __str__(self) -> str:
        return f"{self.name} - {self.description} ({self.is_active})"
    
    def __repr__(self) -> str:
        return f"<Category {self.name} - ({self.id})>"
    
    def get_name(self):
        