#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SceneChecking" for configuration "MinSizeRel"
set_property(TARGET SceneChecking APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SceneChecking PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SceneChecking.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SceneChecking.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SceneChecking )
list(APPEND _IMPORT_CHECK_FILES_FOR_SceneChecking "${_IMPORT_PREFIX}/lib/SceneChecking.lib" "${_IMPORT_PREFIX}/bin/SceneChecking.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
