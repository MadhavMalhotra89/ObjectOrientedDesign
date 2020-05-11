from abc import ABCMeta
from enum import Enum

class RequestStatus(Enum):
  UNREAD = 0
  READ = 1
  ACCEPTED = 2
  REJECTED = 3

