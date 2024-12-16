(function($) {
    $(document).ready(function() {
        $('#id_language').change(function() {
            const languageId = $(this).val();
            const topicField = $('#id_topic');

            topicField.empty();  // Clear the topic dropdown
            if (languageId) {
                $.ajax({
                    url: '/admin/main/topic/',  // Correct URL for fetching topics
                    data: { 'language_id': languageId },
                    success: function(data) {
                        topicField.append('<option value="">---------</option>');
                        if (data.results.length > 0) {
                            data.results.forEach(function(item) {
                                topicField.append(`<option value="${item.id}">${item.text}</option>`);
                            });
                        } else {
                            topicField.append('<option value="">No topics available</option>');  // In case no topics are found
                        }
                    }
                });
            } else {
                topicField.append('<option value="">---------</option>');  // Default empty option
            }
        });

        $('#id_topic').change(function() {
            const topicId = $(this).val();
            const subtopicField = $('#id_subtopic');

            subtopicField.empty();  // Clear the subtopic dropdown
            if (topicId) {
                $.ajax({
                    url: '/admin/main/subtopic/',  // Correct URL for fetching subtopics
                    data: { 'topic_id': topicId },
                    success: function(data) {
                        subtopicField.append('<option value="">---------</option>');
                        if (data.results.length > 0) {
                            data.results.forEach(function(item) {
                                subtopicField.append(`<option value="${item.id}">${item.text}</option>`);
                            });
                        } else {
                            subtopicField.append('<option value="">No subtopics available</option>');  // In case no subtopics are found
                        }
                    }
                });
            } else {
                subtopicField.append('<option value="">---------</option>');  // Default empty option
            }
        });
    });
})(django.jQuery);
