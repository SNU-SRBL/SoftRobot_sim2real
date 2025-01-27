#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaSimpleFem" for configuration "MinSizeRel"
set_property(TARGET SofaSimpleFem APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaSimpleFem PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaSimpleFem.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaSimpleFem.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaSimpleFem )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaSimpleFem "${_IMPORT_PREFIX}/lib/SofaSimpleFem.lib" "${_IMPORT_PREFIX}/bin/SofaSimpleFem.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
