import logging
import os
import sys

from .scrapers.coursefinder import CourseFinder
from .scrapers.calendar.utsg import UTSGCalendar
from .scrapers.timetable.utm import UTMTimetable
from .scrapers.timetable.utsc import UTSCTimetable
from .scrapers.timetable.utsg import UTSGTimetable
from .scrapers.buildings import Buildings
from .scrapers.food import Food
from .scrapers.textbooks import Textbooks
from .scrapers.exams.utsg import UTSGExams
from .scrapers.exams.utm import UTMExams
from .scrapers.exams.utsc import UTSCExams


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger("uoftscrapers").addHandler(NullHandler())
