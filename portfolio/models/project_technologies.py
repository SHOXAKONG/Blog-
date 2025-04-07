from common.models import BaseModel
from django.db import models
from .project import Project
from .technologies import Technologies


class ProjectTechnologies(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    technologies = models.ForeignKey(Technologies, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'project_technologies'