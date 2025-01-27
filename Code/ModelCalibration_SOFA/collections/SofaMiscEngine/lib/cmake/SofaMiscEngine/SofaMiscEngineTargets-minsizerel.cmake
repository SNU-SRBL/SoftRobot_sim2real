#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaMiscEngine" for configuration "MinSizeRel"
set_property(TARGET SofaMiscEngine APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaMiscEngine PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaMiscEngine.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaMiscEngine.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaMiscEngine )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaMiscEngine "${_IMPORT_PREFIX}/lib/SofaMiscEngine.lib" "${_IMPORT_PREFIX}/bin/SofaMiscEngine.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
