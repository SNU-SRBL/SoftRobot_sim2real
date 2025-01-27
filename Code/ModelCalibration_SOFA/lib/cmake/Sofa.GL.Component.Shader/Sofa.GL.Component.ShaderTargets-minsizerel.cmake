#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.GL.Component.Shader" for configuration "MinSizeRel"
set_property(TARGET Sofa.GL.Component.Shader APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.GL.Component.Shader PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.GL.Component.Shader.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.GL.Component.Shader.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.GL.Component.Shader )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.GL.Component.Shader "${_IMPORT_PREFIX}/lib/Sofa.GL.Component.Shader.lib" "${_IMPORT_PREFIX}/bin/Sofa.GL.Component.Shader.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
