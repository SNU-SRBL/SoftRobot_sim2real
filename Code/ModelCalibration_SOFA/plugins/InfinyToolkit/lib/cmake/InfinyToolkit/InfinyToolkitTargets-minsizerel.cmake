#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "InfinyToolkit" for configuration "MinSizeRel"
set_property(TARGET InfinyToolkit APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(InfinyToolkit PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/InfinyToolkit.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/InfinyToolkit.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS InfinyToolkit )
list(APPEND _IMPORT_CHECK_FILES_FOR_InfinyToolkit "${_IMPORT_PREFIX}/lib/InfinyToolkit.lib" "${_IMPORT_PREFIX}/bin/InfinyToolkit.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
