#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaMiscMapping" for configuration "MinSizeRel"
set_property(TARGET SofaMiscMapping APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaMiscMapping PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaMiscMapping.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaMiscMapping.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaMiscMapping )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaMiscMapping "${_IMPORT_PREFIX}/lib/SofaMiscMapping.lib" "${_IMPORT_PREFIX}/bin/SofaMiscMapping.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
