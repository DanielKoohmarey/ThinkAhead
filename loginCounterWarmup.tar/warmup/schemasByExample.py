#-- Conviva Touchstone
#-- Copyright Conviva Inc. 2013
#-- Author: George Necula
#--
# Version 1.2, Oct. 25, 2013
#
import types, copy
import json
import sys



"""
\page schema_by_example Schemas By Example

Schemas-by-example is a library for validating JSON schemas based on schema specifications in the form of examples.

Schemas are high-level description of structured objects. A schema defines the type of the object and its components,
additional validation conditions, and documentation strings. A schema can be used for validation, and also to generate documentation.

There is a standard for [JSON schemas](http://json-schema.org/) but I found it too tedious to write those complex schemas.
Plus, the standard does not easily support conditional schemas where a base schema is extended if certain fields have certain values.
Instead, this module is designed with the following features in mind:
  - A schema can be created by simply saving an example data and pasting it as a Python "repr" value.
  - It should be easy to define schema extensions based on conditionals on object data. For example, if the field 'type' has
    value 'cake', then there should also be a numeric field named 'calories' in the object. This is useful for example
    when defining multiple versions of a schema that can co-exist.
  - It should be easy to augment a simple schema with annotation about optional fields, documentation strings, and extra
    validators.
  - The schemas can be built programatically since they are Python data structures.
  - It should be easy to generate documentation for schemas.


An example of a simple schema is:

    schema1 = { 'ver' : 5,
      'bar' : [ { 'field1' : 'string',
                  'field2' : True
                }
              ]
    }

    Schema.validate(schema1, someObject, objName="theObject")
    html = Schema.htmlDoc(schema1)

The schema above will validate a dictionary with a field 'ver' of numeric type, and a field 'bar', whose type is
a list of zero or more dictionaries, each with two fields, 'field1' of type string, and 'field2' of type boolean.

We describe below the different kinds of schema elements and how they validate:

<table>
<tr>
   <th>Schema example<th>Schema kind<th>Validation
<tr>
   <td>5<td>integer value<td>any number (integer, long, float)
<tr>
   <td>True<td>boolean value<td>any boolean
<tr>
   <td>"string"<td>string value<td>any string
<tr>
   <td>[ ]<td>empty list value<td>any list or tuple. No validation for the list elements.
<tr>
   <td>[ S ]<td>list with one schema<td>a list or tuple, the schema is used to validate __all__ the list elements.
<tr>
   <td>[ S1, S2 ]<td>list with more than one schema<td>a list or tuple with same number of elements as the schema, and each element is validated with the corresponding schema element
<tr>
   <td>( S1, S2 )<td>tuple with more than one schema<td>same as [ S1, S2 ]
<tr>
   <td>{ }<td>empty dictionary<td>any dictionary. No validation for the dictionary values
<tr>
   <td>{ 'key1' : S1, 'key2' : S2}<td>non-empty dictionary with string keys<td>a dictionary with the same keys as the schema. The schema elements are used to validate the dictionary values
<tr>
   <td>{ Schema.allValues : S }</td>
       <td>dictionary with one element with the special key Schema.allValues</td>
       <td>A dictionary used as a collection, the schema element is used to validate the values of the dictionary</td>
<tr>
   <td>None<td> <td>any value, with a warning. Use Schema.anything instead
<tr>
   <td>Schema.anything</td> <td></td> <td>any value</td>
<tr>
   <td>Schema(S, ...)</td>
   <td>An object version of the schema S, with more features<td>Validates like S, except that ... can specify additional documentation and validation options:
             <ul>
                 <li> doc='something' : specify some documentation for this field
                 <li> opt=True : specify that the field may be missing. Makes sense for the schema for a field in a dictionary
                 <li> nullable=True : the value may be null (None in Python)
                 <li> valid=[] : either one additional SchemaValidator, or a list of SchemaValidator

             </ul>
  </td>
  </tr>
<tr>
   <td>S.when(...cond..., doc=str, update=dict)</td>
                 <td>S must be a Schema object for a dictionary schema. The value of the update parameter is a dictionary</td>
                 <td>Evaluates the condition ...cond... on the actual object to be validated, and if true, then validates with S.update(dict), otherwise with S. You can
                 specify a documentation string for this extension.
                 All conditions must be true for the update to take effect. The conditions can be of the form:
                 <ul>
                    <li> field__exists = True : if the field exists in the object.
                    <li> field__neq = val : if the field does not have the given value. Also true if the field does not exist.
                    <li> field__eq = val : if the field has the given value.
                    <li> field__notin = [ vals ] : if the field is not equal to any of the list elements. Also true if the field does not exist.
                    <li> field__geq = val : if the field is greater-or-equal to the given value.
                    <li> field__leq = val : if the field is less-or-equal to the given value.
                 </ul>
                 In the update dictionary you can specify new fields not already in S, or you can override fields already in S.
</table>

Following is an example of a more elaborate schema, with some documentation strings, and marking some fields optional and nullable:

    schema2 = { 'ver' : Schema(5, doc='The value of the version parameter'),
                  'bar' : [ { 'field1' : Schema('string', nullable=True),
                              'field2' : Schema(True, opt=True)
                            }
                          ],
                  'baz' : barElements
    }


And now an example using extensions

    schema3 = Schema(schema2, doc='Base schema').when(ver__geq=2, doc="Version 2",
                                                      update={
                                                         'field3' : "a new string field",
                                                         'field4' : Schema(12, nullable=True)
                                                      }
                                                 ).when(ver__geq=2, field4__exists=True, doc="Version 2, when field4 exists",
                                                      update={
                                                          'field4' : Schema(0, valid=SchemaValidator.geq(0)),
                                                          'field3' : 5
                                                      })

In the above example we extended schema2 with two additional variants, one when the version field 'ver' is greater-or-equal to 2, and
one when also field4 is part of the object. In the latter case, field3 will override the specification to make the field non-nullable.


For further documentation check out the implementation in classes Schema and SchemaValidator.


"""


class Schema:
    """
    The main class
    """

    def __init__(self, sch, doc=None, opt=None, nullable=None, valid=None):
        """
        Extend a schema with additional conditions
        @param sch : the schema to extend
        @param doc : a description of this value
        @param opt : whether the field is optional
        @param nullable : whether the field can be null (None)
        @param valid : a list of validators
        @return an extended schema
        """

        if isinstance(sch, Schema):
            # If we are wrapping a Schema, copy the data
            self.schDelegate = sch.schDelegate
            self.opt = sch.opt
            self.nullable = sch.nullable
            self.valid = sch.valid
            self.doc   = sch.doc
        else:
            self.schDelegate = Schema._delegateForBaseSchema(sch)
            self.opt = False
            self.nullable = False
            self.valid = []
            self.doc = ''

        # Update the parameters
        if doc is not None:
            self.doc = doc
        if opt is not None:
            self.opt = opt
        if nullable is not None:
            self.nullable = nullable
        if valid is not None:
            if isinstance(valid, list):
                self.valid = self.valid + valid
            else:
                self.valid = self.valid + [ valid ]


    """
    A special key to use in a dictionary schema to specify the schema to be used for all values in the dictionary
    """
    allValues = '__allValues'

    """
    A special key to use in a dictionary schema to specify that more keys are allowed
    """
    additionalProperties = '__additionalProperties'


    """
    A special schema that matches any value
    """
    anything  = '__any'

    # A function that is called with (msg, isWarning=False)
    _errorReporter = None

    @staticmethod
    def registerErrorReporter(func):
        Schema._errorReporter = func

    @staticmethod
    def _delegateForBaseSchema(sch):
        """
        Compute the SchemaDelegate for the base schema
        @param sch:
        @return:
        """
        # Compute the delegate
        if isinstance(sch, bool):
            schDelegate = _SchemaTypeBool(sch)
        elif isinstance(sch, int) or isinstance(sch, float):
            schDelegate = _SchemaTypeNumber(sch)
        elif sch == Schema.anything:
            schDelegate = _SchemaAnything(sch)
        elif isinstance(sch, basestring):
            schDelegate = _SchemaTypeString(sch)
        elif isinstance(sch, list):
            schDelegate = _SchemaTypeList(sch)
        elif isinstance(sch, tuple):
            schDelegate = _SchemaTypeList(list(sch))
        elif isinstance(sch, dict):
            schDelegate = _SchemaTypeDict(sch)
        elif sch is None:
            schDelegate = _SchemaNone(sch)
        else:
            assert False
        return schDelegate

    def when(self, update={}, doc="", **condArgs):
        """
        Make a new Schema that is like the existing one except it implements a conditional
        update of the dictionary fields
        @param update: the dictionary to update with
        @param doc: a documentation string
        @param condArgs: the conditions when the update applies
        @return: a new Schema
        """
        assert isinstance(self.schDelegate, _SchemaTypeDict), "The 'when' condition is allowed only on dictionary schemas"
        # Make a clone
        clone = Schema(self)
        updateData = SchemaUpdateData(doc=doc, update=update, **condArgs)

        # replace the delegate
        clone.schDelegate = clone.schDelegate.makeWhen(updateData)
        return clone


    @staticmethod
    def validate(sch, obj, objName='unnamed'):
        """
        Validate an object with a schema
        @param sch : the schema
        @param obj : the object to be validated
        @param objName : the object name, will be used in the error messages
        @return True if the validation passed
        """
        if isinstance(sch, Schema):
            schDelegate = sch.schDelegate
            isNullable  = sch.nullable
            isOptional  = sch.opt
            valid       = sch.valid
        else:
            schDelegate = Schema._delegateForBaseSchema(sch)
            isNullable  = False
            isOptional  = False
            valid       = []

        hadErrors = False
        if obj is None and isNullable:
            return True

        failedType = schDelegate.checkType(obj)
        if failedType is not None:
            Schema._errorMessage(failedType+" (is "+repr(obj)+") for "+objName)
            hadErrors = True
        else:
            if not schDelegate.extraValidations(obj, objName=objName):
                hadErrors = True

            # Now run the configured validators
            if valid:
                hadErrors = False
                for v in valid:
                    if not v._validate(obj, objName=objName):
                        hadErrors = True

            if not schDelegate.recurse(obj, objName=objName):
                hadErrors = True

        return not hadErrors

    def __getitem__(self, attr):
        """
        For dict schemas, we allow their use as a dictionary
        @param attr:
        @return:
        """
        if isinstance(self.schDelegate, _SchemaTypeDict):
            return self.schDelegate.getDictAttr(attr)
        else:
            Schema._errorMessage("Cannot use __getattr__ except on dictionary schemas")

    def __setitem__(self, key, value):
        """
        For dict schemas, we allow their use as a dictionary
        @param key:
        @param value:
        @return:
        """
        if key in ('schDelegate', 'nullable', 'valid', 'opt', 'doc'):
            self.__dict__[key] = value
            return

        if isinstance(self.schDelegate, _SchemaTypeDict):
            self.schDelegate.setDictAttr(key, value)
        else:
            Schema._errorMessage("Cannot use __setattr__ except on dictionary schemas")

    @staticmethod
    def _isOptional(sch):
        if isinstance(sch, Schema):
            return sch.opt
        else:
            return False


    @staticmethod
    def _errorMessage(msg, isWarning=False):
        msg = "Schema: "+msg
        if Schema._errorReporter is None:
            if isWarning:
                msg = "WARNING: "+msg
            else:
                msg = "ERROR: "+msg
            sys.stderr.write(msg)
        else:
            theErrorReporter = Schema.__dict__["_errorReporter"]
            theErrorReporter(msg, isWarning=isWarning)


    @staticmethod
    def _htmlDoc(accum, sch, fieldName=None, depth=0):
        """
        Accumulate to the accum list, strings for rendering this schema in HTML
        """
        if isinstance(sch, Schema):
            schDelegate = sch.schDelegate
            isNullable  = sch.nullable
            isOptional  = sch.opt
            valid       = sch.valid
            doc         = sch.doc
        else:
            schDelegate = Schema._delegateForBaseSchema(sch)
            isNullable  = False
            isOptional  = False
            valid       = []
            doc         = ''

        _SchemaDoc.oneEntryStart(accum, fieldName, schDelegate.htmlDocSummary(), opt=isOptional, nullable=isNullable, doc=doc, depth=depth)
        closing = schDelegate.htmlDocRecurse(accum, depth=depth)
        _SchemaDoc.oneEntryEnd(accum, depth=depth)
        if closing:
            _SchemaDoc.oneEntryEmpty(accum, closing, depth=depth)

    @staticmethod
    def htmlDoc(sch):
        """
        Render the schema documentation as HTML
        """
        accum = []
        _SchemaDoc.schemaEntriesHeader(accum)
        Schema._htmlDoc(accum, sch, depth=0)
        _SchemaDoc.schemaEntriesFooter(accum)
        return "".join(accum)


    @staticmethod
    def unionDict(dict1, dict2):
        """
        Utility function: Return the union of two dictionaries. Like dict.update, except it
        does not change dict and returns the result
        """
        assert isinstance(dict1, dict)
        assert isinstance(dict2, dict)
        res = copy.deepcopy(dict1)
        res.update(dict2)
        return res

class SchemaValidator:
    """
    Additional schema validations
    """
    def __init__(self, fnc, msg):
        """
        A generic schema validator
        @param fnc: a function that takes the object and return True if the validation passes
        @param msg: a message to be used in the error message to explain what failed
        """
        self._fnc = fnc
        self._msg = msg
        self._nested = [ ]


    def _validate(self, obj, objName="unnamed"):
        if not self._fnc(obj):
            Schema._errorMessage("expected "+self._msg+" (is "+repr(obj)+") for "+objName)
            return False
        else:
            return True


    @staticmethod
    def eq(v, msg=None):
        """
        Validates when it is equal to a value
        """
        if msg is None:
            msg = "equal to "+unicode(v)
        return SchemaValidator(lambda obj: obj == v,
                               msg)

    @staticmethod
    def geq(v, msg=None):
        """
        Validates >= to a value
        """
        if msg is None:
            msg = "greater of equal to "+unicode(v)
        return SchemaValidator(lambda obj: obj >= v,
                               msg)

    @staticmethod
    def among(setOfValues, msg=None):
        """
        Validates that a value is among a specified set
        @param setOfValues: a list of acceptable values
        @param msg: the message displayed when validation fails
        @return:
        """
        if msg is None:
            msg = "among the set "+repr(setOfValues)
        return SchemaValidator(lambda obj: obj in setOfValues, msg=msg)


    @staticmethod
    def isEpoch(msg=None):
        """
        Validates an epoch (seconds since 1970)
        @param msg:
        """
        if msg is None:
            msg = "a Unix epoch"
        return SchemaValidator.geq(1300000000, msg=msg)


class SchemaUpdateData:
    """
    Encapsulates the data for the "when-update" extension
    """
    def __init__(self, doc="", update={}, **condArgs):
        self.doc = doc
        self.update = update
        self.condArgs = condArgs


#! \cond PRIVATE

class SchemaContext:
    """
    The superclass for the arguments that can be passed to the schema generators
    """
    def __init__(self):
        pass

    def cond(self, **kwargs):
        """
        Use this function to implement conditional that depend on the contents of the object being validated. The arguments can be
        - field__exists=True  : true when the field exists in the object
        - field__eq=v : true when the field has the given value. Implies field__exists=True
        """
        assert False, "Must override"





class _ContextObject(SchemaContext):
    def __init__(self, obj):
        SchemaContext.__init__(self)
        self.obj = obj

    def cond(self, condArgs):
        for k in condArgs:
            ksplit = k.split("__")
            assert len(ksplit) == 2, "invalid key in conditional: "+k
            if ksplit[1] == "exists":
                if condArgs[k]:
                    # Check that it exists
                    if not ksplit[0] in self.obj:
                        return False
                else:
                    if ksplit[0] in self.obj:
                        return False

            elif ksplit[1] == "eq":
                if not (ksplit[0] in self.obj and self.obj[ksplit[0]] == condArgs[k]):
                    return False

            elif ksplit[1] == "neq":
                if (ksplit[0] in self.obj and self.obj[ksplit[0]] == condArgs[k]):
                    return False

            elif ksplit[1] == 'leq':
                if not (ksplit[0] in self.obj and self.obj[ksplit[0]] <= condArgs[k]):
                    return False

            elif ksplit[1] == 'geq':
                if not (ksplit[0] in self.obj and self.obj[ksplit[0]] >= condArgs[k]):
                    return False

            elif ksplit[1] == 'in':
                if not (ksplit[0] in self.obj and self.obj[ksplit[0]] in condArgs[k]):
                    return False

            elif ksplit[1] == 'notin':
                if (ksplit[0] in self.obj and self.obj[ksplit[0]] in condArgs[k]):
                    return False
            else:
                assert False, "Unexpected predicate "+k
        return True

    @staticmethod
    def condToText(condArgs):
        conds = [ ]
        for k in condArgs:
            ksplit = k.split("__")
            assert len(ksplit) == 2, "invalid key in conditional: "+k
            if ksplit[1] == "exists":
                if condArgs[k]:
                    conds.append("'"+ksplit[0]+"' exists")
                else:
                    conds.append("'"+ksplit[0]+"' does not exist")

            elif ksplit[1] == "eq":
                conds.append("'"+ksplit[0]+"' == "+repr(condArgs[k]))


            elif ksplit[1] == "neq":
                conds.append("'"+ksplit[0]+"' != "+repr(condArgs[k]))

            elif ksplit[1] == "geq":
                conds.append("'"+ksplit[0]+"' >= "+repr(condArgs[k]))

            elif ksplit[1] == "leq":
                conds.append("'"+ksplit[0]+"' <= "+repr(condArgs[k]))

            elif ksplit[1] == "in":
                conds.append("'"+ksplit[0]+"' in "+repr(condArgs[k]))

            elif ksplit[1] == "notin":
                conds.append("'"+ksplit[0]+"' not in "+repr(condArgs[k]))

            else:
                assert False, "Unexpected predicate "+k
        return " and ".join(conds)

class _SchemaDelegate:
    """
    The super class of schema delegates (which actually do the work)
    """
    def __init__(self, baseSchema):
        self.sch = baseSchema
        self.schType = type(baseSchema)
        self.typeName = ""

    def checkType(self, obj):
        """
        Checks the type of the object. Return None if matches, or a string error message
        @param obj:
        @return:
        """
        if isinstance(obj, self.schType):
            return None
        else:
            return "expecting a "+self.typeName

    def extraValidations(self, obj, objName="unnamed"):
        return True

    def recurse(self, obj, objName="unnamed"):
        return True

    def htmlDocSummary(self):
        """
        A one-line summary , or start, of the schema
        @return:
        """
        return json.dumps(self.sch)

    def htmlDocRecurse(self, accum, depth=0):
        return ""

class _SchemaAnything(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)


    def checkType(self, obj):
        return None


class _SchemaNone(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)

    def checkType(cls, obj):
        return None

    def extraValidations(self, obj, objName="unnamed"):
        Schema._errorMessage('using schema None for '+objName, isWarning=True)


class _SchemaTypeNumber(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)
        self.typeName = "number"


    def checkType(self, obj):
        # Strange that in python a boolean appears to be instance of int
        if (isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, long)) and not isinstance(obj, bool):
            return None
        else:
            return "expecting a number"



class _SchemaTypeString(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)
        self.typeName = "string"
        self.schType = basestring



class _SchemaTypeBool(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)
        self.typeName = "boolean"
        self.schType = bool


class _SchemaTypeDict(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)
        # We maintain a list of pairs: (conditionArgs, dict)
        self.updates = [ ]
        self.schType = dict
        self.typeName = "dictionary"

    def getDictAttr(self, item):
        return self.sch[item]

    def setDictAttr(self, key, value):
        self.sch[key] = value


    def makeWhen(self, updateData):
        assert isinstance(updateData, SchemaUpdateData)

        clone = _SchemaTypeDict(self.sch)
        assert not (Schema.allValues in self.sch or Schema.allValues in updateData.update), "Cannot apply 'when' update on dictionaries that contain "+Schema.allValues

        clone.updates = self.updates + [updateData]
        return clone


    def recurse(self, obj, objName=''):
        if len(self.sch) == 0:
            # Do not check values
            return True
        hadErrors = False
        if len(self.sch) == 1 and Schema.allValues in self.sch:
            # Apply the same schema to all values
            for k in obj:
                if not Schema.validate(self.sch[Schema.allValues], obj[k], objName=objName+"."+unicode(k)):
                    hadErrors = True

        else:
            checkedFields = { } # Keep track of the fields we have seen
            # First process the updates, the last one is done first
            if self.updates:
                ctx = _ContextObject(obj)
                for updateIdx in range(len(self.updates) - 1, -1, -1):
                    updateData = self.updates[updateIdx]
                    if ctx.cond(updateData.condArgs):
                        if not self._checkFields(updateData.update, obj, objName=objName, checkedFields=checkedFields):
                            hadErrors = True
            # Now check the base dict
            if not self._checkFields(self.sch, obj, objName=objName, checkedFields=checkedFields):
                hadErrors = True

            for fname in obj:
                if fname not in checkedFields:
                    Schema._errorMessage("found unexpected field "+objName+"."+unicode(fname)+" in "+repr(obj))
                    hadErrors = True

        return not hadErrors


    def _checkFields(self, fieldDict, obj, objName="unnamed", checkedFields={}):
        """
        Check the given fieldDict, skip the ones already in checkedFields
        @param obj:
        @param fields:
        @param objName:
        @param checkedFields:
        @return:
        """
        hadErrors = False
        for schk, schv in fieldDict.iteritems():
            if schk in checkedFields:
                continue
            checkedFields[schk] = True

            if schk not in obj:
                if not Schema._isOptional(schv):
                    Schema._errorMessage("missing non-optional field "+objName+"."+unicode(schk)+" in "+repr(obj))
                    hadErrors = True
            else:
                checkedFields[schk] = True
                if not Schema.validate(schv, obj[schk], objName=objName+"."+unicode(schk)):
                    hadErrors = True
        return not hadErrors


    def htmlDocSummary(self):
        if len(self.sch) == 0:
            # Do not check values
            return "{ * }"
        else:
            return "{"

    def htmlDocRecurse(self, accum, depth=0):
        if len(self.sch) == 0:
            return ""
        if len(self.sch) == 1 and Schema.allValues in self.sch:
            Schema._htmlDoc(accum, self.sch[Schema.allValues], fieldName="*", depth=depth+1)
        else:
            self._htmlDocRecurseFields(accum, self.sch, depth=depth)
            # Now see if we need to do some conditionals
            for updateData in self.updates:
                _SchemaDoc.oneEntryExtension(accum, condition=_ContextObject.condToText(updateData.condArgs), doc=updateData.doc, depth=depth)
                self._htmlDocRecurseFields(accum, updateData.update, depth=depth)
        return "}"

    def _htmlDocRecurseFields(self, accum, fieldDict, depth=0):
        keys = fieldDict.keys()
        for schk in sorted(keys):
            Schema._htmlDoc(accum, fieldDict[schk], fieldName=unicode(schk), depth=depth+1)


class _SchemaTypeList(_SchemaDelegate):
    def __init__(self, sch):
        _SchemaDelegate.__init__(self, sch)
        self.schType = list
        self.typeName = "list"

    def checkType(self, obj):
        # Strange that in python a boolean appears to be instance of int
        if isinstance(obj, list) or isinstance(obj, tuple):
            return None
        else:
            return "expecting a list or tuple"

    def recurse(self, obj, objName=''):
        if len(self.sch) == 0:
            # Do not check values
            return True
        hadErrors = False
        if len(self.sch) == 1:
            # Apply the same schema to all values
            for i in range(len(obj)):
                if not Schema.validate(self.sch[0], obj[i], objName=objName+"["+str(i)+"]"):
                    hadErrors = True
            return not hadErrors
        else:
            # The lengths must match
            if len(self.sch) != len(obj):
                Schema._errorMessage('length of list object (%d) does not match length of schema list (%d) for %s' % (len(obj), len(self.sch), objName))
                hadErrors = True
            else:
                for i in range(len(obj)):
                    if not Schema.validate(self.sch[i], obj[i], objName=objName+"["+str(i)+"]"):
                        hadErrors = True
            return not hadErrors

    def htmlDocSummary(self):
        if len(self.sch) == 0:
            return "[ * ]"
        else:
            return "["


    def htmlDocRecurse(self, accum, depth=0):
        if len(self.sch) == 0:
            return ""
        if len(self.sch) == 1:
            Schema._htmlDoc(accum, self.sch[0], fieldName="[*]", depth=depth+1)
        else:
            for i in range(len(self.sch)):
                Schema._htmlDoc(accum, self.sch[i], fieldName="["+str(i)+"]", depth=depth+1)
        return "]"

schemaDocStyle = """
<style>
    .sbe-header {
        background-color: rgb(152, 223, 220);
    }


    .sbe-schema {
        border-right: 1px solid black;
        border-bottom: 1px solid black;
        min-width: 650px;
    }

    .sbe-entry {
        border-top: 1px solid black;
        border-left: 1px solid black;
        display: block;
    }



    .sbe-entry .sbe-entry  {
        /* Nested entries are indented and with no borders */
        margin-left: 30px;
        border-bottom: none;
        border-right: none;
    }


    .sbe-entry .sbe-extension {
        background-color : pink;
    }

    .sbe-extension .sbe-cond {
        display: inline-block;

    }

    .sbe-extension .sbe-conddoc {
        display: inline-block;
        border-left: 1px solid black;
        text-align: center;
        padding-left: 4px;
    }

    .sbe-entry .sbe-field-example {
        display: inline-block;
        vertical-align: top;
        padding: 2px;
        width: 500px;
    }

    .sbe-entry .sbe-field-example .sbe-fieldname {
        color: blue;
    }

    .sbe-entry .sbe-entry .sbe-field-example  {
        width: 469px;
    }
    .sbe-entry .sbe-entry .sbe-entry .sbe-field-example  {
        width: 438px;
    }
    .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-field-example {
        width: 407px;
    }
    .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-field-example  {
        width: 376px;
    }
    .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-field-example  {
        width: 345px;
    }
    .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-entry .sbe-field-example  {
        width: 314px;
    }

    .sbe-entry .columns {
        display: inline-block;
        margin-bottom: -4px;
    }

    .sbe-entry .optional {
        display: table-cell;
        border-left: 1px solid black;
        height: 100%;
        text-align: center;
        width: 40px;
    }

    .sbe-entry .nullable {
        display: table-cell;
        border-left: 1px solid black;
        text-align: center;
        width: 40px;
        height: 100%;
    }

    .sbe-entry .doc {
        padding: 2px;
        display: table-cell;
        border-left: 1px solid black;
        width: 400px;
        height: 100%

    }
</style>
<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<script type='text/javascript'>
    $(document).ready(function () {
        $(".sbe-entry .sbe-field-example a").click(function (e) {
           var p = $(this).parent().parent();
           var summary = $(".summary", $(this).parent());
           if(p.attr('childrenAreHidden') == '1') {
              $(".sbe-entry", p).show ();
              p.attr('childrenAreHidden', '0');
              var summaryHtml = summary.html();
              summary.html(summaryHtml.replace("...", ""));

           } else {
              $(".sbe-entry", p).hide ();
              p.attr('childrenAreHidden', '1');
              summary.html(summary.html() + " ...");
           }
           e.stopPropagation();
           e.preventDefault ();
           return false;
        });
    });
</script>
"""

class _SchemaDoc:

    @staticmethod
    def oneEntryStart(accum, fieldName, summary, opt=False, nullable=False, doc="", depth=0):
        """
        Generate one documentation entry
        @param fieldName:
        @param summary:
        @param opt:
        @param nullable:
        @param doc:
        @return:
        """

        if isinstance(opt, basestring):
            reqOpt = opt
        elif opt:
            reqOpt = "Y"
        else:
            reqOpt = ""

        if isinstance(nullable, basestring):
            nullRender = nullable
        elif nullable:
            nullRender = "Y"
        else:
            nullRender = ""

        fieldNameRender = summary
        if fieldName is not None:
            if summary == "{" or summary == "[":
                fieldNameRender = "<a href=''><span class='sbe-fieldname'>"+fieldName+"</span></a> : <span class='summary'>"+summary+"</span>"
            else:
                fieldNameRender = "<span class='sbe-fieldname'>"+fieldName+"</span> : "+summary
        else:
            fieldNameRender = summary

        indent=(" "*(depth * 2))
        indent1=indent + "  "

        if nullRender == "" and doc == "" and reqOpt == "":
            # We have to put something or else the box disapears
            doc="<div style='height:14px'></div>"
        accum += [
            indent,
            "<div class='sbe-entry'>\n", indent1,"<div class='sbe-field-example'>", fieldNameRender, "</div>\n",
            indent1,"<div class='columns'>\n",indent1,"  <div class='optional'>", reqOpt,
            "</div>\n",indent1,"  <div class='nullable'>", nullRender, "</div>\n",indent1,"  <div class='doc'>", unicode(doc), "</div>\n",indent1,"</div>\n"
        ]

    @staticmethod
    def oneEntryExtension(accum, condition="", doc="", depth=0):
        indent=(" "*(depth * 2))
        accum += [indent,"  <div class='sbe-entry sbe-extension'><div class='sbe-field-example'>Extension fields when: ",condition,"</div><div class='columns'><div class='sbe-conddoc'>",doc,"</div></div></div>\n"]

    @staticmethod
    def oneEntryEmpty(accum, text="", depth=0):
        indent=(" "*(depth * 2))
        accum += [indent,"  <div class='sbe-entry sbe-empty'>",text,"</div>\n"]


    @staticmethod
    def oneEntryEnd(accum, depth=0):
        indent=(" "*(depth * 2))
        accum += [indent,"</div>\n"]


    @staticmethod
    def schemaEntriesHeader(accum):
        accum += [
            "<div class='sbe-schema'>"
            "<div class='sbe-header'>"
        ]
        _SchemaDoc.oneEntryStart(accum, fieldName=None, summary="Field : Example-Value", opt="Opt?", nullable="Null?", doc="Description")
        _SchemaDoc.oneEntryEnd(accum)
        accum += [
            "</div>"
        ]

    @staticmethod
    def schemaEntriesFooter(accum):
        accum += [
            "</div>"
        ]


#! \endcond PRIVATE