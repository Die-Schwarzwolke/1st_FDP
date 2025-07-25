from converter import m_to_ft, ft_to_m

def test_roundtrip_one_meter():
    assert abs(ft_to_m(m_to_ft(1.0)) - 1.0) < 1e-6

def test_specific_value():
    assert abs(ft_to_m(3.28084) - 1.0) < 1e-5