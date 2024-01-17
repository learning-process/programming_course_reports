cmake_minimum_required( VERSION 3.27 )

message( STATUS "Programming Course Reports" )
project(programming_course_reports)

include(${CMAKE_SOURCE_DIR}/cmake/configure.cmake)

############################### LATEX ###############################
option(USE_LATEX OFF)
if( USE_LATEX )
    find_package(LATEX REQUIRED)
endif( USE_LATEX )

add_subdirectory(modules)
