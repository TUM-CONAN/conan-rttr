#include <iostream>
#include <string>

#include <rttr/registration>
#include <rttr/type>

using namespace rttr;

struct point2d
{
    point2d() {}
    point2d(int x_, int y_) : x(x_), y(y_) {}
    int x = 0;
    int y = 0;
};


RTTR_REGISTRATION
{
    rttr::registration::class_<point2d>("point2d")
        .constructor()(rttr::policy::ctor::as_object)
        .property("x", &point2d::x)
        .property("y", &point2d::y)
        ;
}

int main(){
	point2d p(1,1);

	rttr::instance obj2 = p;
	rttr::instance obj = obj2.get_type().get_raw_type().is_wrapper() ? obj2.get_wrapped_instance() : obj2;

	auto prop_list = obj.get_derived_type().get_properties();
    for (auto prop : prop_list)
    {
        const auto name = prop.get_name();
        std::cout << name << std::endl;
    }

	return 0;
}