# coding: utf-8
from abc import abstractclassmethod


class BaseSort(object):
  @abstractclassmethod
  def sort(self, array=[]):
    pass
