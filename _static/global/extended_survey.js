// compatible otree>=5.2.0

var op_checker = function op_checker(radio_id, op_id) {
  var radio_tag = "#" + radio_id;
  var op_tag = "#" + op_id;
  var radio_parent = $(radio_tag).parent().parent().parent();

  var set_current_status = function set_current_status() {
    if ($(radio_tag).is(":checked")) {
      console.log(radio_tag+" was checked")
      $(op_tag).show();
    } else {
      $(op_tag).hide();
    }
  };

  set_current_status();
  radio_parent.change(function () {
    set_current_status();
  });

  $("input:radio").change(function () {
    set_current_status();
  });
};

var show_after = function show_after(id, seconds) {
  var tag = "#" + id;
  $(tag).delay(seconds * 1000).fadeIn();
};

var checkbox_hider = function checkbox_hider(checkbox_id, receiver_id) {
  var checkbox_tag = "#" + checkbox_id;
  var receiver_tag = "#" + receiver_id;
  $(checkbox_tag).change(function () {
    // console.log(checkbox_tag + " changed");

    if ($(checkbox_tag).is(":checked")) {
      $(receiver_tag).val(0).hide();
    } else {
      $(receiver_tag).show();
    }
  });
};

var checkbox_shower = function checkbox_shower(checkbox_id, receiver_id) {
  var checkbox_tag = "#" + checkbox_id;
  var receiver_tag = "#" + receiver_id;
  $(checkbox_tag).change(function () {
    // console.log(checkbox_tag + " changed");

    if ($(checkbox_tag).is(":checked")) {
      $(receiver_tag).show();
    } else {
      $(receiver_tag).hide();
    }
  });
};

var hide_others = function hide_others(tag_list, num_choices_to_hide) {
  $('input:radio').change(function (e) {
    // console.log("hide_others(): started for "+tag_list);

    var selected_id = $(this).parent().parent().attr('id');
    // console.log("selected_id="+selected_id);

    var index_of_selected_id = tag_list.indexOf(selected_id);
    // console.log("index_of_selected_id="+index_of_selected_id);

    if (index_of_selected_id >= 0) {
      var _loop = function _loop(i) {
        // console.log("checking order "+i+"...");
        tag_list.forEach(function (tag, index, array) {
          if (is_unchecked_all(tag_list, i)) {
            $(radio_tag_maker(tag, i)).attr("disabled", false);
          } else {
            if ($(radio_tag_maker(tag, i)).is(":checked")) {
              $(radio_tag_maker(tag, i)).attr("disabled", false);
            } else {
              $(radio_tag_maker(tag, i)).attr("disabled", true);
            }
          }
        });
      };

      // console.log("loop entered:");
      for (var i = 0; i < num_choices_to_hide; i++) {
        _loop(i);
      }
    }
  });
};

var hide_others2 = function hide_others(tag_list, num_choices_to_hide) {
  $('input:radio').change(function (e) {
    console.log("hide_others(): started for "+tag_list);

    var selected_id = $(this).parent().attr('id');
    console.log("selected_id="+selected_id);

    var index_of_selected_id = tag_list.indexOf(selected_id);
    console.log("index_of_selected_id="+index_of_selected_id);

    if (index_of_selected_id >= 0) {
      var _loop = function _loop(i) {
        console.log("checking order "+i+"...");
        tag_list.forEach(function (tag, index, array) {
          if (is_unchecked_all(tag_list, i)) {
            $(radio_tag_maker(tag, i)).attr("disabled", false);
          } else {
            if ($(radio_tag_maker(tag, i)).is(":checked")) {
              $(radio_tag_maker(tag, i)).attr("disabled", false);
            } else {
              $(radio_tag_maker(tag, i)).attr("disabled", true);
            }
          }
        });
      };

      // console.log("loop entered:");
      for (var i = 0; i < num_choices_to_hide; i++) {
        _loop(i);
      }
    }
  });
};

var is_unchecked_all = function is_unchecked_all(tag_list, i) {
  // console.log("is_unchecked_all: i=",i);
  if (tag_list.every(function (item, index, array) {
    if ($(radio_tag_maker(item, i)).is(":checked")) {
      // console.log("false return");
      return false;
    } else {
      return true;
    }
  })) {
    // console.log("true return, and exit is_unchecked_all");
    return true;
  } else {
    // console.log("false return, and exit is_unchecked_all");
    return false;
  }
  // console.log("true return");
  return true;
};

var radio_tag_maker = function radio_tag_maker(tag, i) {
  // console.log("radio_tag:"+ "#" + tag + "-" + i);
  return "#" + tag + "-" + i;
};