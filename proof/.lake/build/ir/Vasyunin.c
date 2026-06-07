// Lean compiler output
// Module: Vasyunin
// Imports: public import Init public meta import Init public import Mathlib.Analysis.SpecialFunctions.Integrals.Basic public import Mathlib.MeasureTheory.Measure.Lebesgue.Basic public import Mathlib.Topology.ContinuousMap.Basic public import Mathlib.Analysis.InnerProductSpace.Basic public import Lean.Data.Json
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* lp_mathlib_Nat_cast___at___00MeasureTheory_SimpleFunc_ennrealRatEmbed_spec__2(lean_object*);
uint8_t lean_usize_dec_lt(size_t, size_t);
lean_object* lean_array_uget_borrowed(lean_object*, size_t);
lean_object* l_Lean_Json_getArr_x3f(lean_object*);
lean_object* lean_array_uset(lean_object*, size_t, lean_object*);
lean_object* lean_array_get_borrowed(lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Json_getInt_x3f(lean_object*);
lean_object* lean_array_get(lean_object*, lean_object*, lean_object*);
lean_object* l_Rat_ofInt(lean_object*);
uint8_t l_instDecidableEqRat_decEq(lean_object*, lean_object*);
lean_object* l_Rat_div(lean_object*, lean_object*);
size_t lean_usize_add(size_t, size_t);
lean_object* lean_array_get_size(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* l_Lean_Json_parse(lean_object*);
size_t lean_array_size(lean_object*);
lean_object* l_IO_FS_readFile(lean_object*);
lean_object* lean_mk_empty_array_with_capacity(lean_object*);
static lean_once_cell_t lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0;
static const lean_string_object lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 27, .m_capacity = 27, .m_length = 26, .m_data = "Denominator cannot be zero"};
static const lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__1 = (const lean_object*)&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__1_value;
static const lean_ctor_object lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 0}, .m_objs = {((lean_object*)&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__1_value)}};
static const lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__2 = (const lean_object*)&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__2_value;
static const lean_string_object lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 25, .m_capacity = 25, .m_length = 24, .m_data = "Expected [num, den] pair"};
static const lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__3 = (const lean_object*)&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__3_value;
static const lean_ctor_object lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 0}, .m_objs = {((lean_object*)&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__3_value)}};
static const lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__4 = (const lean_object*)&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__4_value;
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0(size_t, size_t, lean_object*);
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0(size_t, size_t, lean_object*);
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_RiemannProof_parseCoefficients(lean_object*);
LEAN_EXPORT lean_object* lp_RiemannProof_readCoefficients(lean_object*);
LEAN_EXPORT lean_object* lp_RiemannProof_readCoefficients___boxed(lean_object*, lean_object*);
static const lean_array_object lp_RiemannProof_vasyunin__json__array___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_array_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 246}, .m_size = 0, .m_capacity = 0, .m_data = {}};
static const lean_object* lp_RiemannProof_vasyunin__json__array___closed__0 = (const lean_object*)&lp_RiemannProof_vasyunin__json__array___closed__0_value;
LEAN_EXPORT const lean_object* lp_RiemannProof_vasyunin__json__array = (const lean_object*)&lp_RiemannProof_vasyunin__json__array___closed__0_value;
static lean_object* _init_lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0(void){
_start:
{
lean_object* v___x_1_; lean_object* v___x_2_; 
v___x_1_ = lean_unsigned_to_nat(0u);
v___x_2_ = lp_mathlib_Nat_cast___at___00MeasureTheory_SimpleFunc_ennrealRatEmbed_spec__2(v___x_1_);
return v___x_2_;
}
}
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0(size_t v_sz_9_, size_t v_i_10_, lean_object* v_bs_11_){
_start:
{
uint8_t v___x_12_; 
v___x_12_ = lean_usize_dec_lt(v_i_10_, v_sz_9_);
if (v___x_12_ == 0)
{
lean_object* v___x_13_; 
v___x_13_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_13_, 0, v_bs_11_);
return v___x_13_;
}
else
{
lean_object* v_v_14_; lean_object* v___x_15_; 
v_v_14_ = lean_array_uget_borrowed(v_bs_11_, v_i_10_);
lean_inc(v_v_14_);
v___x_15_ = l_Lean_Json_getArr_x3f(v_v_14_);
if (lean_obj_tag(v___x_15_) == 0)
{
lean_object* v_a_16_; lean_object* v___x_18_; uint8_t v_isShared_19_; uint8_t v_isSharedCheck_23_; 
lean_dec_ref(v_bs_11_);
v_a_16_ = lean_ctor_get(v___x_15_, 0);
v_isSharedCheck_23_ = !lean_is_exclusive(v___x_15_);
if (v_isSharedCheck_23_ == 0)
{
v___x_18_ = v___x_15_;
v_isShared_19_ = v_isSharedCheck_23_;
goto v_resetjp_17_;
}
else
{
lean_inc(v_a_16_);
lean_dec(v___x_15_);
v___x_18_ = lean_box(0);
v_isShared_19_ = v_isSharedCheck_23_;
goto v_resetjp_17_;
}
v_resetjp_17_:
{
lean_object* v___x_21_; 
if (v_isShared_19_ == 0)
{
v___x_21_ = v___x_18_;
goto v_reusejp_20_;
}
else
{
lean_object* v_reuseFailAlloc_22_; 
v_reuseFailAlloc_22_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_22_, 0, v_a_16_);
v___x_21_ = v_reuseFailAlloc_22_;
goto v_reusejp_20_;
}
v_reusejp_20_:
{
return v___x_21_;
}
}
}
else
{
lean_object* v_a_24_; lean_object* v___x_25_; lean_object* v___x_26_; lean_object* v_bs_x27_27_; lean_object* v___x_62_; lean_object* v___x_63_; uint8_t v___x_64_; 
v_a_24_ = lean_ctor_get(v___x_15_, 0);
lean_inc(v_a_24_);
lean_dec_ref_known(v___x_15_, 1);
v___x_25_ = lean_box(0);
v___x_26_ = lean_unsigned_to_nat(0u);
v_bs_x27_27_ = lean_array_uset(v_bs_11_, v_i_10_, v___x_26_);
v___x_62_ = lean_array_get_size(v_a_24_);
v___x_63_ = lean_unsigned_to_nat(2u);
v___x_64_ = lean_nat_dec_eq(v___x_62_, v___x_63_);
if (v___x_64_ == 0)
{
if (v___x_12_ == 0)
{
goto v___jp_28_;
}
else
{
lean_object* v___x_65_; 
lean_dec_ref(v_bs_x27_27_);
lean_dec(v_a_24_);
v___x_65_ = ((lean_object*)(lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__4));
return v___x_65_;
}
}
else
{
goto v___jp_28_;
}
v___jp_28_:
{
lean_object* v___x_29_; lean_object* v___x_30_; 
v___x_29_ = lean_array_get_borrowed(v___x_25_, v_a_24_, v___x_26_);
lean_inc(v___x_29_);
v___x_30_ = l_Lean_Json_getInt_x3f(v___x_29_);
if (lean_obj_tag(v___x_30_) == 0)
{
lean_object* v_a_31_; lean_object* v___x_33_; uint8_t v_isShared_34_; uint8_t v_isSharedCheck_38_; 
lean_dec_ref(v_bs_x27_27_);
lean_dec(v_a_24_);
v_a_31_ = lean_ctor_get(v___x_30_, 0);
v_isSharedCheck_38_ = !lean_is_exclusive(v___x_30_);
if (v_isSharedCheck_38_ == 0)
{
v___x_33_ = v___x_30_;
v_isShared_34_ = v_isSharedCheck_38_;
goto v_resetjp_32_;
}
else
{
lean_inc(v_a_31_);
lean_dec(v___x_30_);
v___x_33_ = lean_box(0);
v_isShared_34_ = v_isSharedCheck_38_;
goto v_resetjp_32_;
}
v_resetjp_32_:
{
lean_object* v___x_36_; 
if (v_isShared_34_ == 0)
{
v___x_36_ = v___x_33_;
goto v_reusejp_35_;
}
else
{
lean_object* v_reuseFailAlloc_37_; 
v_reuseFailAlloc_37_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_37_, 0, v_a_31_);
v___x_36_ = v_reuseFailAlloc_37_;
goto v_reusejp_35_;
}
v_reusejp_35_:
{
return v___x_36_;
}
}
}
else
{
lean_object* v_a_39_; lean_object* v___x_40_; lean_object* v___x_41_; lean_object* v___x_42_; 
v_a_39_ = lean_ctor_get(v___x_30_, 0);
lean_inc(v_a_39_);
lean_dec_ref_known(v___x_30_, 1);
v___x_40_ = lean_unsigned_to_nat(1u);
v___x_41_ = lean_array_get(v___x_25_, v_a_24_, v___x_40_);
lean_dec(v_a_24_);
v___x_42_ = l_Lean_Json_getInt_x3f(v___x_41_);
if (lean_obj_tag(v___x_42_) == 0)
{
lean_object* v_a_43_; lean_object* v___x_45_; uint8_t v_isShared_46_; uint8_t v_isSharedCheck_50_; 
lean_dec(v_a_39_);
lean_dec_ref(v_bs_x27_27_);
v_a_43_ = lean_ctor_get(v___x_42_, 0);
v_isSharedCheck_50_ = !lean_is_exclusive(v___x_42_);
if (v_isSharedCheck_50_ == 0)
{
v___x_45_ = v___x_42_;
v_isShared_46_ = v_isSharedCheck_50_;
goto v_resetjp_44_;
}
else
{
lean_inc(v_a_43_);
lean_dec(v___x_42_);
v___x_45_ = lean_box(0);
v_isShared_46_ = v_isSharedCheck_50_;
goto v_resetjp_44_;
}
v_resetjp_44_:
{
lean_object* v___x_48_; 
if (v_isShared_46_ == 0)
{
v___x_48_ = v___x_45_;
goto v_reusejp_47_;
}
else
{
lean_object* v_reuseFailAlloc_49_; 
v_reuseFailAlloc_49_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_49_, 0, v_a_43_);
v___x_48_ = v_reuseFailAlloc_49_;
goto v_reusejp_47_;
}
v_reusejp_47_:
{
return v___x_48_;
}
}
}
else
{
lean_object* v_a_51_; lean_object* v___x_52_; lean_object* v___x_53_; uint8_t v___x_54_; 
v_a_51_ = lean_ctor_get(v___x_42_, 0);
lean_inc(v_a_51_);
lean_dec_ref_known(v___x_42_, 1);
v___x_52_ = l_Rat_ofInt(v_a_51_);
v___x_53_ = lean_obj_once(&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0, &lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0_once, _init_lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0);
v___x_54_ = l_instDecidableEqRat_decEq(v___x_52_, v___x_53_);
if (v___x_54_ == 0)
{
lean_object* v___x_55_; lean_object* v___x_56_; size_t v___x_57_; size_t v___x_58_; lean_object* v___x_59_; 
v___x_55_ = l_Rat_ofInt(v_a_39_);
v___x_56_ = l_Rat_div(v___x_55_, v___x_52_);
lean_dec_ref(v___x_55_);
v___x_57_ = ((size_t)1ULL);
v___x_58_ = lean_usize_add(v_i_10_, v___x_57_);
v___x_59_ = lean_array_uset(v_bs_x27_27_, v_i_10_, v___x_56_);
v_i_10_ = v___x_58_;
v_bs_11_ = v___x_59_;
goto _start;
}
else
{
lean_object* v___x_61_; 
lean_dec_ref(v___x_52_);
lean_dec(v_a_39_);
lean_dec_ref(v_bs_x27_27_);
v___x_61_ = ((lean_object*)(lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__2));
return v___x_61_;
}
}
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___boxed(lean_object* v_sz_66_, lean_object* v_i_67_, lean_object* v_bs_68_){
_start:
{
size_t v_sz_boxed_69_; size_t v_i_boxed_70_; lean_object* v_res_71_; 
v_sz_boxed_69_ = lean_unbox_usize(v_sz_66_);
lean_dec(v_sz_66_);
v_i_boxed_70_ = lean_unbox_usize(v_i_67_);
lean_dec(v_i_67_);
v_res_71_ = lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0(v_sz_boxed_69_, v_i_boxed_70_, v_bs_68_);
return v_res_71_;
}
}
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0(size_t v_sz_72_, size_t v_i_73_, lean_object* v_bs_74_){
_start:
{
uint8_t v___x_75_; 
v___x_75_ = lean_usize_dec_lt(v_i_73_, v_sz_72_);
if (v___x_75_ == 0)
{
lean_object* v___x_76_; 
v___x_76_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_76_, 0, v_bs_74_);
return v___x_76_;
}
else
{
lean_object* v_v_77_; lean_object* v___x_78_; 
v_v_77_ = lean_array_uget_borrowed(v_bs_74_, v_i_73_);
lean_inc(v_v_77_);
v___x_78_ = l_Lean_Json_getArr_x3f(v_v_77_);
if (lean_obj_tag(v___x_78_) == 0)
{
lean_object* v_a_79_; lean_object* v___x_81_; uint8_t v_isShared_82_; uint8_t v_isSharedCheck_86_; 
lean_dec_ref(v_bs_74_);
v_a_79_ = lean_ctor_get(v___x_78_, 0);
v_isSharedCheck_86_ = !lean_is_exclusive(v___x_78_);
if (v_isSharedCheck_86_ == 0)
{
v___x_81_ = v___x_78_;
v_isShared_82_ = v_isSharedCheck_86_;
goto v_resetjp_80_;
}
else
{
lean_inc(v_a_79_);
lean_dec(v___x_78_);
v___x_81_ = lean_box(0);
v_isShared_82_ = v_isSharedCheck_86_;
goto v_resetjp_80_;
}
v_resetjp_80_:
{
lean_object* v___x_84_; 
if (v_isShared_82_ == 0)
{
v___x_84_ = v___x_81_;
goto v_reusejp_83_;
}
else
{
lean_object* v_reuseFailAlloc_85_; 
v_reuseFailAlloc_85_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_85_, 0, v_a_79_);
v___x_84_ = v_reuseFailAlloc_85_;
goto v_reusejp_83_;
}
v_reusejp_83_:
{
return v___x_84_;
}
}
}
else
{
lean_object* v_a_87_; lean_object* v___x_88_; lean_object* v___x_89_; lean_object* v_bs_x27_90_; lean_object* v___x_125_; lean_object* v___x_126_; uint8_t v___x_127_; 
v_a_87_ = lean_ctor_get(v___x_78_, 0);
lean_inc(v_a_87_);
lean_dec_ref_known(v___x_78_, 1);
v___x_88_ = lean_box(0);
v___x_89_ = lean_unsigned_to_nat(0u);
v_bs_x27_90_ = lean_array_uset(v_bs_74_, v_i_73_, v___x_89_);
v___x_125_ = lean_array_get_size(v_a_87_);
v___x_126_ = lean_unsigned_to_nat(2u);
v___x_127_ = lean_nat_dec_eq(v___x_125_, v___x_126_);
if (v___x_127_ == 0)
{
if (v___x_75_ == 0)
{
goto v___jp_91_;
}
else
{
lean_object* v___x_128_; 
lean_dec_ref(v_bs_x27_90_);
lean_dec(v_a_87_);
v___x_128_ = ((lean_object*)(lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__4));
return v___x_128_;
}
}
else
{
goto v___jp_91_;
}
v___jp_91_:
{
lean_object* v___x_92_; lean_object* v___x_93_; 
v___x_92_ = lean_array_get_borrowed(v___x_88_, v_a_87_, v___x_89_);
lean_inc(v___x_92_);
v___x_93_ = l_Lean_Json_getInt_x3f(v___x_92_);
if (lean_obj_tag(v___x_93_) == 0)
{
lean_object* v_a_94_; lean_object* v___x_96_; uint8_t v_isShared_97_; uint8_t v_isSharedCheck_101_; 
lean_dec_ref(v_bs_x27_90_);
lean_dec(v_a_87_);
v_a_94_ = lean_ctor_get(v___x_93_, 0);
v_isSharedCheck_101_ = !lean_is_exclusive(v___x_93_);
if (v_isSharedCheck_101_ == 0)
{
v___x_96_ = v___x_93_;
v_isShared_97_ = v_isSharedCheck_101_;
goto v_resetjp_95_;
}
else
{
lean_inc(v_a_94_);
lean_dec(v___x_93_);
v___x_96_ = lean_box(0);
v_isShared_97_ = v_isSharedCheck_101_;
goto v_resetjp_95_;
}
v_resetjp_95_:
{
lean_object* v___x_99_; 
if (v_isShared_97_ == 0)
{
v___x_99_ = v___x_96_;
goto v_reusejp_98_;
}
else
{
lean_object* v_reuseFailAlloc_100_; 
v_reuseFailAlloc_100_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_100_, 0, v_a_94_);
v___x_99_ = v_reuseFailAlloc_100_;
goto v_reusejp_98_;
}
v_reusejp_98_:
{
return v___x_99_;
}
}
}
else
{
lean_object* v_a_102_; lean_object* v___x_103_; lean_object* v___x_104_; lean_object* v___x_105_; 
v_a_102_ = lean_ctor_get(v___x_93_, 0);
lean_inc(v_a_102_);
lean_dec_ref_known(v___x_93_, 1);
v___x_103_ = lean_unsigned_to_nat(1u);
v___x_104_ = lean_array_get(v___x_88_, v_a_87_, v___x_103_);
lean_dec(v_a_87_);
v___x_105_ = l_Lean_Json_getInt_x3f(v___x_104_);
if (lean_obj_tag(v___x_105_) == 0)
{
lean_object* v_a_106_; lean_object* v___x_108_; uint8_t v_isShared_109_; uint8_t v_isSharedCheck_113_; 
lean_dec(v_a_102_);
lean_dec_ref(v_bs_x27_90_);
v_a_106_ = lean_ctor_get(v___x_105_, 0);
v_isSharedCheck_113_ = !lean_is_exclusive(v___x_105_);
if (v_isSharedCheck_113_ == 0)
{
v___x_108_ = v___x_105_;
v_isShared_109_ = v_isSharedCheck_113_;
goto v_resetjp_107_;
}
else
{
lean_inc(v_a_106_);
lean_dec(v___x_105_);
v___x_108_ = lean_box(0);
v_isShared_109_ = v_isSharedCheck_113_;
goto v_resetjp_107_;
}
v_resetjp_107_:
{
lean_object* v___x_111_; 
if (v_isShared_109_ == 0)
{
v___x_111_ = v___x_108_;
goto v_reusejp_110_;
}
else
{
lean_object* v_reuseFailAlloc_112_; 
v_reuseFailAlloc_112_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_112_, 0, v_a_106_);
v___x_111_ = v_reuseFailAlloc_112_;
goto v_reusejp_110_;
}
v_reusejp_110_:
{
return v___x_111_;
}
}
}
else
{
lean_object* v_a_114_; lean_object* v___x_115_; lean_object* v___x_116_; uint8_t v___x_117_; 
v_a_114_ = lean_ctor_get(v___x_105_, 0);
lean_inc(v_a_114_);
lean_dec_ref_known(v___x_105_, 1);
v___x_115_ = l_Rat_ofInt(v_a_114_);
v___x_116_ = lean_obj_once(&lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0, &lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0_once, _init_lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__0);
v___x_117_ = l_instDecidableEqRat_decEq(v___x_115_, v___x_116_);
if (v___x_117_ == 0)
{
lean_object* v___x_118_; lean_object* v___x_119_; size_t v___x_120_; size_t v___x_121_; lean_object* v___x_122_; lean_object* v___x_123_; 
v___x_118_ = l_Rat_ofInt(v_a_102_);
v___x_119_ = l_Rat_div(v___x_118_, v___x_115_);
lean_dec_ref(v___x_118_);
v___x_120_ = ((size_t)1ULL);
v___x_121_ = lean_usize_add(v_i_73_, v___x_120_);
v___x_122_ = lean_array_uset(v_bs_x27_90_, v_i_73_, v___x_119_);
v___x_123_ = lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0(v_sz_72_, v___x_121_, v___x_122_);
return v___x_123_;
}
else
{
lean_object* v___x_124_; 
lean_dec_ref(v___x_115_);
lean_dec(v_a_102_);
lean_dec_ref(v_bs_x27_90_);
v___x_124_ = ((lean_object*)(lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00__private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0_spec__0___closed__2));
return v___x_124_;
}
}
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0___boxed(lean_object* v_sz_129_, lean_object* v_i_130_, lean_object* v_bs_131_){
_start:
{
size_t v_sz_boxed_132_; size_t v_i_boxed_133_; lean_object* v_res_134_; 
v_sz_boxed_132_ = lean_unbox_usize(v_sz_129_);
lean_dec(v_sz_129_);
v_i_boxed_133_ = lean_unbox_usize(v_i_130_);
lean_dec(v_i_130_);
v_res_134_ = lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0(v_sz_boxed_132_, v_i_boxed_133_, v_bs_131_);
return v_res_134_;
}
}
LEAN_EXPORT lean_object* lp_RiemannProof_parseCoefficients(lean_object* v_s_135_){
_start:
{
lean_object* v___x_136_; 
v___x_136_ = l_Lean_Json_parse(v_s_135_);
if (lean_obj_tag(v___x_136_) == 0)
{
lean_object* v_a_137_; lean_object* v___x_139_; uint8_t v_isShared_140_; uint8_t v_isSharedCheck_144_; 
v_a_137_ = lean_ctor_get(v___x_136_, 0);
v_isSharedCheck_144_ = !lean_is_exclusive(v___x_136_);
if (v_isSharedCheck_144_ == 0)
{
v___x_139_ = v___x_136_;
v_isShared_140_ = v_isSharedCheck_144_;
goto v_resetjp_138_;
}
else
{
lean_inc(v_a_137_);
lean_dec(v___x_136_);
v___x_139_ = lean_box(0);
v_isShared_140_ = v_isSharedCheck_144_;
goto v_resetjp_138_;
}
v_resetjp_138_:
{
lean_object* v___x_142_; 
if (v_isShared_140_ == 0)
{
v___x_142_ = v___x_139_;
goto v_reusejp_141_;
}
else
{
lean_object* v_reuseFailAlloc_143_; 
v_reuseFailAlloc_143_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_143_, 0, v_a_137_);
v___x_142_ = v_reuseFailAlloc_143_;
goto v_reusejp_141_;
}
v_reusejp_141_:
{
return v___x_142_;
}
}
}
else
{
lean_object* v_a_145_; lean_object* v___x_146_; 
v_a_145_ = lean_ctor_get(v___x_136_, 0);
lean_inc(v_a_145_);
lean_dec_ref_known(v___x_136_, 1);
v___x_146_ = l_Lean_Json_getArr_x3f(v_a_145_);
if (lean_obj_tag(v___x_146_) == 0)
{
lean_object* v_a_147_; lean_object* v___x_149_; uint8_t v_isShared_150_; uint8_t v_isSharedCheck_154_; 
v_a_147_ = lean_ctor_get(v___x_146_, 0);
v_isSharedCheck_154_ = !lean_is_exclusive(v___x_146_);
if (v_isSharedCheck_154_ == 0)
{
v___x_149_ = v___x_146_;
v_isShared_150_ = v_isSharedCheck_154_;
goto v_resetjp_148_;
}
else
{
lean_inc(v_a_147_);
lean_dec(v___x_146_);
v___x_149_ = lean_box(0);
v_isShared_150_ = v_isSharedCheck_154_;
goto v_resetjp_148_;
}
v_resetjp_148_:
{
lean_object* v___x_152_; 
if (v_isShared_150_ == 0)
{
v___x_152_ = v___x_149_;
goto v_reusejp_151_;
}
else
{
lean_object* v_reuseFailAlloc_153_; 
v_reuseFailAlloc_153_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_153_, 0, v_a_147_);
v___x_152_ = v_reuseFailAlloc_153_;
goto v_reusejp_151_;
}
v_reusejp_151_:
{
return v___x_152_;
}
}
}
else
{
lean_object* v_a_155_; size_t v_sz_156_; size_t v___x_157_; lean_object* v___x_158_; 
v_a_155_ = lean_ctor_get(v___x_146_, 0);
lean_inc(v_a_155_);
lean_dec_ref_known(v___x_146_, 1);
v_sz_156_ = lean_array_size(v_a_155_);
v___x_157_ = ((size_t)0ULL);
v___x_158_ = lp_RiemannProof___private_Init_Data_Array_Basic_0__Array_mapMUnsafe_map___at___00parseCoefficients_spec__0(v_sz_156_, v___x_157_, v_a_155_);
return v___x_158_;
}
}
}
}
LEAN_EXPORT lean_object* lp_RiemannProof_readCoefficients(lean_object* v_path_159_){
_start:
{
lean_object* v___x_161_; 
v___x_161_ = l_IO_FS_readFile(v_path_159_);
if (lean_obj_tag(v___x_161_) == 0)
{
lean_object* v_a_162_; lean_object* v___x_164_; uint8_t v_isShared_165_; uint8_t v_isSharedCheck_182_; 
v_a_162_ = lean_ctor_get(v___x_161_, 0);
v_isSharedCheck_182_ = !lean_is_exclusive(v___x_161_);
if (v_isSharedCheck_182_ == 0)
{
v___x_164_ = v___x_161_;
v_isShared_165_ = v_isSharedCheck_182_;
goto v_resetjp_163_;
}
else
{
lean_inc(v_a_162_);
lean_dec(v___x_161_);
v___x_164_ = lean_box(0);
v_isShared_165_ = v_isSharedCheck_182_;
goto v_resetjp_163_;
}
v_resetjp_163_:
{
lean_object* v___x_166_; 
v___x_166_ = lp_RiemannProof_parseCoefficients(v_a_162_);
if (lean_obj_tag(v___x_166_) == 0)
{
lean_object* v_a_167_; lean_object* v___x_169_; uint8_t v_isShared_170_; uint8_t v_isSharedCheck_177_; 
v_a_167_ = lean_ctor_get(v___x_166_, 0);
v_isSharedCheck_177_ = !lean_is_exclusive(v___x_166_);
if (v_isSharedCheck_177_ == 0)
{
v___x_169_ = v___x_166_;
v_isShared_170_ = v_isSharedCheck_177_;
goto v_resetjp_168_;
}
else
{
lean_inc(v_a_167_);
lean_dec(v___x_166_);
v___x_169_ = lean_box(0);
v_isShared_170_ = v_isSharedCheck_177_;
goto v_resetjp_168_;
}
v_resetjp_168_:
{
lean_object* v___x_172_; 
if (v_isShared_170_ == 0)
{
lean_ctor_set_tag(v___x_169_, 18);
v___x_172_ = v___x_169_;
goto v_reusejp_171_;
}
else
{
lean_object* v_reuseFailAlloc_176_; 
v_reuseFailAlloc_176_ = lean_alloc_ctor(18, 1, 0);
lean_ctor_set(v_reuseFailAlloc_176_, 0, v_a_167_);
v___x_172_ = v_reuseFailAlloc_176_;
goto v_reusejp_171_;
}
v_reusejp_171_:
{
lean_object* v___x_174_; 
if (v_isShared_165_ == 0)
{
lean_ctor_set_tag(v___x_164_, 1);
lean_ctor_set(v___x_164_, 0, v___x_172_);
v___x_174_ = v___x_164_;
goto v_reusejp_173_;
}
else
{
lean_object* v_reuseFailAlloc_175_; 
v_reuseFailAlloc_175_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_175_, 0, v___x_172_);
v___x_174_ = v_reuseFailAlloc_175_;
goto v_reusejp_173_;
}
v_reusejp_173_:
{
return v___x_174_;
}
}
}
}
else
{
lean_object* v_a_178_; lean_object* v___x_180_; 
v_a_178_ = lean_ctor_get(v___x_166_, 0);
lean_inc(v_a_178_);
lean_dec_ref_known(v___x_166_, 1);
if (v_isShared_165_ == 0)
{
lean_ctor_set(v___x_164_, 0, v_a_178_);
v___x_180_ = v___x_164_;
goto v_reusejp_179_;
}
else
{
lean_object* v_reuseFailAlloc_181_; 
v_reuseFailAlloc_181_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_181_, 0, v_a_178_);
v___x_180_ = v_reuseFailAlloc_181_;
goto v_reusejp_179_;
}
v_reusejp_179_:
{
return v___x_180_;
}
}
}
}
else
{
lean_object* v_a_183_; lean_object* v___x_185_; uint8_t v_isShared_186_; uint8_t v_isSharedCheck_190_; 
v_a_183_ = lean_ctor_get(v___x_161_, 0);
v_isSharedCheck_190_ = !lean_is_exclusive(v___x_161_);
if (v_isSharedCheck_190_ == 0)
{
v___x_185_ = v___x_161_;
v_isShared_186_ = v_isSharedCheck_190_;
goto v_resetjp_184_;
}
else
{
lean_inc(v_a_183_);
lean_dec(v___x_161_);
v___x_185_ = lean_box(0);
v_isShared_186_ = v_isSharedCheck_190_;
goto v_resetjp_184_;
}
v_resetjp_184_:
{
lean_object* v___x_188_; 
if (v_isShared_186_ == 0)
{
v___x_188_ = v___x_185_;
goto v_reusejp_187_;
}
else
{
lean_object* v_reuseFailAlloc_189_; 
v_reuseFailAlloc_189_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_189_, 0, v_a_183_);
v___x_188_ = v_reuseFailAlloc_189_;
goto v_reusejp_187_;
}
v_reusejp_187_:
{
return v___x_188_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_RiemannProof_readCoefficients___boxed(lean_object* v_path_191_, lean_object* v_a_192_){
_start:
{
lean_object* v_res_193_; 
v_res_193_ = lp_RiemannProof_readCoefficients(v_path_191_);
lean_dec_ref(v_path_191_);
return v_res_193_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Measure_Lebesgue_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Topology_ContinuousMap_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_InnerProductSpace_Basic(uint8_t builtin);
lean_object* initialize_Lean_Data_Json(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_RiemannProof_Vasyunin(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Measure_Lebesgue_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Topology_ContinuousMap_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_InnerProductSpace_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Lean_Data_Json(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
