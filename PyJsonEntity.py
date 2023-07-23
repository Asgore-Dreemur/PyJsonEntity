import json
class PyJsonEntity:
    @staticmethod
    def JsonToEntity(jsondict: dict, entity):
        def HandleJsonObject(njsondict: dict, jentity):
            nentity = type(jentity)()
            for i in njsondict.items():
                key: str = i[0]
                value = i[1]
                if key in nentity.__dict__.keys():
                    kvalue = nentity.__dict__[key]
                    if "__dict__" in dir(kvalue) and type(value) is dict:
                        setattr(nentity, key, HandleJsonObject(value, kvalue))
                    elif type(kvalue) is dict and len(kvalue) >= 1:
                        setattr(nentity, key, HandleJsonDict(value, list(kvalue.values())[0]))
                    elif type(kvalue) is list and len(kvalue) >= 1:
                        if "__dict__" in dir(kvalue[0]):
                            setattr(nentity, key, HandleJsonList(value, kvalue[0]))
                    else:
                        setattr(nentity, key, value)
            return nentity

        def HandleJsonList(jsonlist:list, jentity):
            jlist: list = []
            for i in jsonlist:
                jlist.append(HandleJsonObject(i, jentity))
            return jlist

        def HandleJsonDict(jsondict:dict, ventity):
            edict: dict = {}
            for i in jsondict.items():
                if type(i[1]) is dict:
                    edict[i[0]] = HandleJsonObject(i[1], ventity)
                else:
                    edict[i[0]] = i[1]
            return edict

        return HandleJsonObject(jsondict, entity)

    @staticmethod
    def EntityToJson(entity):
        def HandleJsonObject(nentity):
            jsondict: dict = {}
            for i in nentity.__dict__.items():
                key = i[0]
                value = i[1]
                if value is not None:
                    if "__dict__" in dir(value):
                        jsondict[key] = HandleJsonObject(value)
                    elif type(value) is list:
                        jsondict[key] = HandleJsonList(value)
                    elif type(value) is dict:
                        jsondict[key] = HandleJsonDict(value)
                    else:
                        jsondict[key] = value
            return jsondict

        def HandleJsonList(hlist: list):
            flist: list = []
            for i in hlist:
                if i is not None:
                    if "__dict__" in dir(i):
                        flist.append(HandleJsonObject(i))
                    elif type(i) is list:
                        flist.append(HandleJsonList(i))
                    elif type(i) is dict:
                        flist.append(HandleJsonDict(i))
                    else:
                        flist.append(i)
            return flist

        def HandleJsonDict(hdict: dict):
            fdict: dict = {}
            for i in hdict.items():
                key = i[0]
                value = i[1]
                if value is not None:
                    if "__dict__" in dir(value):
                        fdict[key] = HandleJsonObject(value)
                    elif type(value) is list:
                        fdict[key] = HandleJsonList(value)
                    elif type(value) is dict:
                        fdict[key] = HandleJsonDict(value)
                    else:
                        fdict[key] = value
            return fdict

        return HandleJsonObject(entity)
