#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main code of sorter app

Author
------
Name
    Berkay Gunduz
GitLab
    berkaygunduz
GitHub
    berkaygunduzz
"""

import os
import time


class Files:
    """
    A class that manages sorting files by last modified date

    ...
    
    Attributes
    ----------
    _files : list
        a list that contains file objects
    _created : list
        a list that contains created folder names
    _smr : list
        a list that contains months of summer
    _wnt : list
        a list that contains months of winter
    _spr : list
        a list that contains months of spring
    _aut : list
        a list that contains months of autumn
    
    Methods
    -------
    _date(m)
        Returns which season is m
    _add_file(file)
        Creates an Files object from a file
    _scan(path)
        Creates Files objects recursively from a directory
    _place()
        Copyies files by their last modified date
    sort(path)
        Function for end user usage
    """

    _files = []
    _created = []

    _smr = ["Jun", "Jul", "Aug"]
    _wnt = ["Dec", "Jan", "Fab"]
    _spr = ["Mar", "Apr", "May"]
    _aut = ["Sep", "Oct", "Nov"]

    def __init__(self, name, date):
        """
        Parameters
        ----------
        name : str
            path and name of file
        date : str
            last modified date of file
        """
        self.name = name
        self.date = date
        Files._files.append(self)

    @classmethod
    def _date(cls, m):
        """Returns season of given string
        
        Parameters
        ----------
        m : str
            Month name to be checked
        """
        if m in Files._smr:
            return "Summer"
        elif m in Files._wnt:
            return "Winter"
        elif m in Files._spr:
            return "Spring"
        elif m in Files._aut:
            return "Autumn"
        else:
            raise print(f"Unrecognized month: {m}")

    @classmethod
    def _add_file(cls, file):
        """Creates an Files object from a file
        
        Parameters
        ----------
        file : str
            Path and name of file
        """
        ti = time.ctime(os.path.getmtime(file))
        s_ti = ti.split()
        date = (f"{s_ti[-1]} {Files._date(s_ti[1])}")
        Files(file, date)

    @classmethod
    def _scan(cls, path):
        """Creates Files objects recursively from a directory
        
        Parameters
        ----------
        path : str
            Path of folder that will be scanned recursively
        """
        os.chdir(path)
        files = list(filter(os.path.isfile, os.listdir()))
        dirs = list(filter(os.path.isdir, os.listdir()))
        for file in files:
            Files._add_file(f"{path}/{file}")
        for directory in dirs:
            Files._scan(f"{path}/{directory}")

    @classmethod
    def _place(cls):
        """Copyies files by their last modified date
        """
        os.chdir("/home/berkay")
        try:
            os.mkdir("Sorted Files")
        except Exception as e:
            print(e)
        os.chdir("./Sorted Files")
        for p in Files._files:
            try:
                date = p.date
                if date in Files._created:
                    file = p.name.replace(" ", "\\ ")
                    time = date.replace(" ", "\\ ")
                    command = f"cp {file} ./{time}"
                    os.system(command)
                else:
                    try:
                        os.mkdir(date)
                    except Exception as e:
                        print(e)
                    Files._created.append(date)
                    file = p.name.replace(" ", "\\ ")
                    time = date.replace(" ", "\\ ")
                    command = f"cp {file} ./{time}"
                    os.system(command)
            except Exception as e:
                print (e)

    @classmethod
    def sort(cls, path):
        """End user function to make all magic happen
        
        Parameters
        ----------
        path : str
            Path of folder that will be sorted and copyied
        """
        Files._files = []
        Files._created = []
        Files._scan(path)
        Files._place()
        print("Process has been completed!")

if __name__ == "__main__":
    Files.sort(input("Please write full path of folder: "))

