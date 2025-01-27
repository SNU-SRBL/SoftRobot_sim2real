#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.GUI.Common" for configuration "MinSizeRel"
set_property(TARGET Sofa.GUI.Common APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.GUI.Common PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.GUI.Common.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.GUI.Common.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.GUI.Common )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.GUI.Common "${_IMPORT_PREFIX}/lib/Sofa.GUI.Common.lib" "${_IMPORT_PREFIX}/bin/Sofa.GUI.Common.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
