from datetime import datetime, timezone

from sqlmodel import Column, DateTime, Field, func
import sqlalchemy
from typing import List

import reflex as rx

   
class Movie(rx.Model, table=True):
    MovieCode: str = Field(unique=True)
    created: datetime = Field(
        datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    updated: datetime = Field(
        datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    Title: str
    image: str
    Year: int
    Genre: str
    Director: str
    Actors: str

    def dict(self, *args, **kwargs) -> dict:
        """Serialize method."""
        d = super().dict(*args, **kwargs)
        d["created"] = self.created.replace(microsecond=0).isoformat()
        d["updated"] = self.updated.replace(microsecond=0).isoformat()
        return d


class DailyOTTRank(rx.Model, table= True):
    rankdate: str
    created: datetime = Field(
        datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    updated: datetime = Field(
        datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

    naver: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    fundex: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    jw: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    def dict(self, *args, **kwargs) -> dict:
        """Serialize method."""
        d = super().dict(*args, **kwargs)
        d["created"] = self.created.replace(microsecond=0).isoformat()
        d["updated"] = self.updated.replace(microsecond=0).isoformat()
        return d
    
    
class DailyDramaRank(rx.Model, table= True):
    rankdate: str = Field(unique = True)
    created: datetime = Field(
        datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    updated: datetime = Field(
        datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    naver: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    fundex: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    jw: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    Wavve: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    KMDB: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    IMDB: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    TMDB: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    Watcha: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    Netflix: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    Tving: List[str] = Field(sa_column=sqlalchemy.Column(sqlalchemy.JSON))
    
    def dict(self, *args, **kwargs) -> dict:
        """Serialize method."""
        d = super().dict(*args, **kwargs)
        d["created"] = self.created.replace(microsecond=0).isoformat()
        d["updated"] = self.updated.replace(microsecond=0).isoformat()
        return d