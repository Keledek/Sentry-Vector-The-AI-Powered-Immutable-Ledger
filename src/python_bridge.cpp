#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "nanodb.hpp"

namespace py = pybind11;

PYBIND11_MODULE(nanodb, m) {
    py::class_<nanodb::SearchResult>(m, "SearchResult")
        .def_readwrite("score", &nanodb::SearchResult::score)
        .def_readwrite("data", &nanodb::SearchResult::data);

    py::class_<nanodb::NanoEngine>(m, "Engine")
        .def(py::init<>())
        .def("insert_vector", &nanodb::NanoEngine::insert_vector)
        .def("semantic_search", &nanodb::NanoEngine::semantic_search)
        .def("verify_chain", &nanodb::NanoEngine::verify_chain)
        .def("get_version", &nanodb::NanoEngine::getVersion);
}
