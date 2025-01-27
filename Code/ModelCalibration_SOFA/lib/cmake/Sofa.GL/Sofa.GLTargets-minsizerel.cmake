#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.GL" for configuration "MinSizeRel"
set_property(TARGET Sofa.GL APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.GL PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.GL.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.GL.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.GL )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.GL "${_IMPORT_PREFIX}/lib/Sofa.GL.lib" "${_IMPORT_PREFIX}/bin/Sofa.GL.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
