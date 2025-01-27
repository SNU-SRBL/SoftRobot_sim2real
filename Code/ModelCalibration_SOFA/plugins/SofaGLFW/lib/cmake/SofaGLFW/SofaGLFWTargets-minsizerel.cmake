#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaGLFW" for configuration "MinSizeRel"
set_property(TARGET SofaGLFW APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaGLFW PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaGLFW.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_MINSIZEREL "glfw"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaGLFW.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaGLFW )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaGLFW "${_IMPORT_PREFIX}/lib/SofaGLFW.lib" "${_IMPORT_PREFIX}/bin/SofaGLFW.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
