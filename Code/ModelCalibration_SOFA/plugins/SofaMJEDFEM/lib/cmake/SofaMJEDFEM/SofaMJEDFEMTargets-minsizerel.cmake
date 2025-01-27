#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaMJEDFEM" for configuration "MinSizeRel"
set_property(TARGET SofaMJEDFEM APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaMJEDFEM PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaMJEDFEM.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaMJEDFEM.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaMJEDFEM )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaMJEDFEM "${_IMPORT_PREFIX}/lib/SofaMJEDFEM.lib" "${_IMPORT_PREFIX}/bin/SofaMJEDFEM.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
