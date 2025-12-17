from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from .corporate_code import CorporateCode


@dataclass
class Corporate:
    id: Optional[int]
    code: CorporateCode
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    events: List = field(default_factory=list)

    @classmethod
    def create(cls, code: CorporateCode, name: str) -> 'Corporate':
        now = datetime.utcnow()
        corporate = cls(
            id=None,
            code=code,
            name=name,
            is_active=True,
            created_at=now,
            updated_at=now,
            events=[]
        )
        # Add event if needed
        return corporate
