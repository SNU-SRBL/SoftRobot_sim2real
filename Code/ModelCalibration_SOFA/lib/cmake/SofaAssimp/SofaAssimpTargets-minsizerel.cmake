#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaAssimp" for configuration "MinSizeRel"
set_property(TARGET SofaAssimp APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaAssimp PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaAssimp.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaAssimp.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaAssimp )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaAssimp "${_IMPORT_PREFIX}/lib/SofaAssimp.lib" "${_IMPORT_PREFIX}/bin/SofaAssimp.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
