#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaEngine" for configuration "MinSizeRel"
set_property(TARGET SofaEngine APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaEngine PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaEngine.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaEngine.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaEngine )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaEngine "${_IMPORT_PREFIX}/lib/SofaEngine.lib" "${_IMPORT_PREFIX}/bin/SofaEngine.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
