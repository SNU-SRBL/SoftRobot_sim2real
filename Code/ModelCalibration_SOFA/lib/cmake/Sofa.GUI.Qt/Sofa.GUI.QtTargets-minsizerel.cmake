#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.GUI.Qt" for configuration "MinSizeRel"
set_property(TARGET Sofa.GUI.Qt APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.GUI.Qt PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.GUI.Qt.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.GUI.Qt.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.GUI.Qt )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.GUI.Qt "${_IMPORT_PREFIX}/lib/Sofa.GUI.Qt.lib" "${_IMPORT_PREFIX}/bin/Sofa.GUI.Qt.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
