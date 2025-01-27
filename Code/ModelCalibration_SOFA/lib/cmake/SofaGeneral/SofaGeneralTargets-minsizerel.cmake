#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaGeneral" for configuration "MinSizeRel"
set_property(TARGET SofaGeneral APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaGeneral PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaGeneral.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaGeneral.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaGeneral )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaGeneral "${_IMPORT_PREFIX}/lib/SofaGeneral.lib" "${_IMPORT_PREFIX}/bin/SofaGeneral.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
