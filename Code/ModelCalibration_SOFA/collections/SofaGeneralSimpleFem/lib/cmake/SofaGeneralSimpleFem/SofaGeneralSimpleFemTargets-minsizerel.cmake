#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaGeneralSimpleFem" for configuration "MinSizeRel"
set_property(TARGET SofaGeneralSimpleFem APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaGeneralSimpleFem PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaGeneralSimpleFem.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaGeneralSimpleFem.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaGeneralSimpleFem )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaGeneralSimpleFem "${_IMPORT_PREFIX}/lib/SofaGeneralSimpleFem.lib" "${_IMPORT_PREFIX}/bin/SofaGeneralSimpleFem.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
