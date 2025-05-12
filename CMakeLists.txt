cmake_minimum_required( VERSION 3.27 )

message( STATUS "Programming Course Reports" )
project(programming_course_reports)

include(${CMAKE_SOURCE_DIR}/cmake/configure.cmake)

############################### LATEX ###############################
option(USE_LATEX ON)
if( USE_LATEX )
    find_package(LATEX REQUIRED)
    if(NOT (LATEX_FOUND AND LATEX_PDFLATEX_FOUND))
        set(USE_LATEX OFF)
    endif()
endif( USE_LATEX )

add_subdirectory(modules)
